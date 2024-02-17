from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from django.dispatch import receiver

from . import get_render_model, get_video_model
from .models import AbstractRender, AbstractVideo, UploadedVideoChunk
from .tasks import encode_video, is_celery_present


@receiver(pre_delete, sender=UploadedVideoChunk)
def on_uploaded_video_chunk_pre_delete(instance: UploadedVideoChunk, *args, **kwargs):
    instance.file.delete(save=False)


@receiver(post_delete, sender=get_video_model())
def on_video_post_delete(instance: AbstractVideo, *args, **kwargs):
    instance.upload.delete()


@receiver(pre_save, sender=get_video_model())
def on_video_pre_save(instance: AbstractVideo, *args, **kwargs):
    """
    Whenever a new uploaded video is assigned to a video, encode that video file
    and generate the new renders.
    """
    if old_instance := get_video_model().objects.filter(id=instance.id).first():
        if old_instance.upload_id != instance.upload_id and is_celery_present():
            encode_video.delay(video_id=instance.id)


@receiver(post_save, sender=get_video_model())
def on_video_post_save(instance: AbstractVideo, created: bool, *args, **kwargs):
    """
    Whenever a video is created, encode the video file and generate the renders.
    """
    if created and is_celery_present():
        encode_video.delay(video_id=instance.id)


@receiver(pre_delete, sender=get_render_model())
def on_render_pre_delete(instance: AbstractRender, *args, **kwargs):
    instance.file.delete(save=False)
