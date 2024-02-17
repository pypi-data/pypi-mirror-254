import subprocess
import uuid
from os import makedirs
from os.path import join
from shutil import rmtree
from subprocess import run
from typing import BinaryIO, Optional

import magic
from django.conf import settings
from django.core.files.base import File
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.db.transaction import atomic

from . import get_render_model, get_video_model
from .codecs import get_presets
from .exceptions import ConfigurationError, InvalidVideoFile
from .models import AbstractRender, AbstractVideo, RemoteVideoFile, lock


def compute_division(division: str) -> Optional[float]:
    if division == "N/A":
        return None

    a, b = division.split("/")
    return float(a) / float(b)


def try_round(n: Optional[float]) -> Optional[float]:
    return round(n, 2) if n is not None else n


def get_video_info(file: BinaryIO) -> dict:
    """
    Uses ffprobe to retrieve some basic information about a video file (size,
    duration...)
    """
    data = None

    if isinstance(file, InMemoryUploadedFile):
        filename = "-"
        position = file.tell()
        file.seek(0)
        data = file.read()
        file.seek(position)
        mime = magic.from_buffer(data, mime=True)
    else:
        filename = (
            file.temporary_file_path()
            if isinstance(file, TemporaryUploadedFile)
            else file.name
        )
        mime = magic.from_file(filename, mime=True)

    ffprobe = run(
        [
            "ffprobe",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,nb_frames,avg_frame_rate:format=duration",
            "-of",
            "default=noprint_wrappers=1",
            filename,
        ],
        input=data,
        capture_output=True,
    )

    info = {
        key: try_round(compute_division(value) if "/" in value else float(value))
        for key, value in (line.split("=") for line in ffprobe.stdout.decode().split())
    }

    if ffprobe.returncode:
        raise InvalidVideoFile

    if not info["nb_frames"]:
        info["nb_frames"] = round(info["avg_frame_rate"] * info["duration"])

    info["mime"] = mime
    # Rename some keys to fit the models used in wideo
    info["frame_count"] = info["nb_frames"]
    info["frames_per_second"] = info["avg_frame_rate"]
    del info["nb_frames"]
    del info["avg_frame_rate"]
    return info


def encode_video(video_id: int):
    """
    Encodes a specific video with whichever presets have been specified in the settings.
    """

    wideo_working_dir = getattr(settings, "WIDEO_WORKING_DIR")
    task_working_dir = join(wideo_working_dir, str(uuid.uuid4()))
    makedirs(task_working_dir)

    if not wideo_working_dir:
        raise ConfigurationError

    with atomic():
        # Before the actual encoding part, flag the video as being processed
        if (
            video := get_video_model()
            .objects.select_for_update()
            .filter(id=video_id)
            .first()
        ):
            video.status = AbstractVideo.ProcessStatus.processing
            video.save()
            # Since we are going to create new renders, delete any previous ones
            get_render_model().objects.filter(video=video).delete()
        else:
            return

    # Encapsulating everything in a separate function makes it easier to try/except, and
    # thus to make sure the status of the video is always changed at the end.
    # noinspection PyBroadException
    try:
        get_video_model().objects.filter(id=video_id).update(
            status=AbstractVideo.ProcessStatus.success
            if encode_video_impl(video, task_working_dir)
            else AbstractVideo.ProcessStatus.failed
        )
    except Exception:
        get_video_model().objects.filter(id=video_id).update(
            status=AbstractVideo.ProcessStatus.failed
        )
        raise
    finally:
        rmtree(task_working_dir)


@lock("encode_video")
def encode_video_impl(video: AbstractVideo, working_dir: str) -> bool:
    """
    The actual implementation of the video encoding using ffmpeg. Return `True` if the
    encoding went down as intended, or `False` if something went wrong.
    """

    presets_map = get_presets()
    renders = {}
    ffmpegs = []

    def abort_everything():
        """
        If something goes wrong during processing (invalid file...), stop everything and
        ensure we don't keep any unused Render objects.
        """
        for f in ffmpegs:
            f.kill()

        for r in renders.values():
            r.delete()

    def get_render_temp_file(r: AbstractRender) -> str:
        """
        Creates a simple unique path to a temporary file, used for storing outputs of
        ffmpeg.
        """
        return join(working_dir, str(r.id))

    # The input file must be written to the disk so that ffmpeg can access it randomly.
    # Streaming the file directly to ffmpeg's stdin would be simpler, but ffmpeg would
    # then not always be able to determine what type of file is its input.

    input_file_path = join(working_dir, "input")

    with open(input_file_path, "wb") as input_file:
        for chunk in video.upload.chunks.order_by("index"):
            with chunk.file.open("rb") as chunk_file:
                input_file.write(chunk_file.read())

    for preset_label, preset in presets_map.items():
        # Fill the render with bogus data until we can get info from the encoded videos
        render = get_render_model().objects.create(
            video=video,
            mime="",
            duration=0,
            width=0,
            height=0,
            frames_per_second=0,
            frame_count=0,
        )
        renders[preset_label] = render
        flags = preset["ffmpeg_flags"]
        command = f"ffmpeg -y -i {input_file_path} -f {preset['extension']} {' '.join(flags)} {get_render_temp_file(render)}"
        ffmpeg = subprocess.Popen(command, shell=True)

        # If parallel work is disabled, wait for each ffmpeg process synchronously to
        # avoid having more than one running at once, and panic if any of them fails.
        # If parallel work is enabled, store the processes to check for their result
        # later on.
        if getattr(settings, "WIDEO_PARALLEL_WORK", False):
            ffmpegs.append(ffmpeg)
        elif ffmpeg.wait():
            abort_everything()
            return False

    # When parallel work is enabled, `ffmpegs` will contain a list with all ffmpeg
    # process that we should wait for. As for when parallel work is disabled, if any of
    # them has failed, panic and abort everything.
    for ffmpeg in ffmpegs:
        if ffmpeg.wait():
            abort_everything()
            return False

    # After all videos have been correctly generated, we just need to write them into
    # their respective Render objects
    for preset_label, preset in presets_map.items():
        render = renders[preset_label]

        with open(get_render_temp_file(render), "rb") as file:
            name = f"{render.video.title}_{preset_label}.{preset['extension']}"
            uploaded_file = File(file)
            # Saving the file this way is necessary; `render.file = File(file, name)`
            # does not work
            render.file.save(name, uploaded_file, save=True)

            # Don't forget to get info from the generated videos, and to store it in the
            # previously created Render objects
            video_info = get_video_info(file)

        for field in RemoteVideoFile.INFORMATION_FIELDS:
            setattr(render, field, video_info[field])

        render.save()

    return True
