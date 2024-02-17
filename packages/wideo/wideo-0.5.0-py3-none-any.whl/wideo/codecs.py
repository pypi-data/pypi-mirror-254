from enum import Enum

from django.conf import settings


class Codec(str, Enum):
    """Available code types."""

    H264 = "H264"
    AV1 = "AV1"


# FFMPEG arguments to be used for each specific codec available
CODEC_ARGS = {
    Codec.H264: ["-c:v", "libx264", "-movflags", "faststart"],
    Codec.AV1: ["-c:v", "libaom-av1", "-b:v", "0"],
}

# Video file extension for each codec type
CODEC_EXTENSION = {Codec.H264: "mp4", Codec.AV1: "webm"}

# Mapping between the quality of a video and the number of pixels to encode
VIDEO_QUALITY_TO_PIXELS = {"4K": "3840", "1080P": "1920", "720P": "1280"}


def build_ffmpeg_codec_args(codec: Codec, quality: str) -> list[str]:
    """
    Given a specific codec and the quality of a video, build the arguments to
    be used in a ffmpeg command to encode the video.
    """

    # Default to 1080P if the specified quality is not correct
    if quality not in VIDEO_QUALITY_TO_PIXELS:
        quality = "1080P"

    pixels = VIDEO_QUALITY_TO_PIXELS[quality]
    extra_args = CODEC_ARGS[codec]

    return [
        "-vf",
        f"\"scale='min({pixels},iw)':min'({pixels},ih)':force_original_aspect_ratio=decrease\"",
        "-preset",
        "veryslow",
        *extra_args,
    ]


def build_preset(codec: Codec, quality: str) -> dict:
    """
    Build a preset object for the given codec and video quality.
    """
    return {
        "ffmpeg_flags": build_ffmpeg_codec_args(codec, quality),
        "codec": f'video/{CODEC_EXTENSION[codec]}; codecs="avc1.42E01E, mp4a.40.2"',
        "extension": CODEC_EXTENSION[codec],
    }


def get_presets() -> dict:
    """
    Retrieve the map of available presets from the Django settings if specified.
    Fallback to the default list of presets.
    """
    presets: dict[str, str | dict] = getattr(settings, "WIDEO_PRESETS", DEFAULT_PRESETS)

    return {
        # If a preset is the name of a default preset, get the preset dict from there
        name: (KNOWN_PRESETS.get(preset) if isinstance(preset, str) else preset)
        for name, preset in presets.items()
    }


KNOWN_PRESETS = {
    "4K_H264": build_preset(Codec.H264, "4K"),
    "1080_H264": build_preset(Codec.H264, "1080P"),
    "1080P_H264": build_preset(Codec.H264, "1080P"),
    "720_H264": build_preset(Codec.H264, "720P"),
    "720P_H264": build_preset(Codec.H264, "720P"),
    "4K_AV1": build_preset(Codec.AV1, "4K"),
    "1080_AV1": build_preset(Codec.AV1, "1080P"),
    "1080P_AV1": build_preset(Codec.AV1, "1080P"),
    "720_AV1": build_preset(Codec.AV1, "720P"),
    "720P_AV1": build_preset(Codec.AV1, "720P"),
}

DEFAULT_PRESETS = {
    name: preset for name, preset in KNOWN_PRESETS.items() if name.endswith("H264")
}
