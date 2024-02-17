from celery import shared_task
from django.conf import settings
from django.db.transaction import atomic


def is_celery_present() -> bool:
    """
    Checks is Celery is supposed to be used. Reasonably, checking `CELERY_BROKER_URL`
    should be a reliable indicator of whether the current project uses Celery or not.
    """
    return bool(getattr(settings, "CELERY_BROKER_URL", False))


@shared_task
def delete_orphan_uploaded_videos():
    from .models import delete_orphan_uploaded_videos

    delete_orphan_uploaded_videos()


@shared_task
@atomic
def encode_video(video_id: int):
    from .ffmpeg import encode_video

    encode_video(video_id)
