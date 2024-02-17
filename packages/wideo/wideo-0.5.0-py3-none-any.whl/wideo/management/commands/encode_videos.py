from django.core.management import BaseCommand
from django.utils.translation import gettext as _

from ... import get_video_model
from ...ffmpeg import encode_video
from ...models import AbstractVideo


class Command(BaseCommand):
    help = _("Encodes any video that has not yet been encoded")

    def handle(self, *args, **options):
        for video_id in (
            get_video_model()
            .objects.filter(status=AbstractVideo.ProcessStatus.pending)
            .values_list("id", flat=True)
        ):
            encode_video(video_id)
