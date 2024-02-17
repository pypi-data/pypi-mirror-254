from django.core.management import BaseCommand
from django.utils.translation import gettext_lazy as _

from ...models import delete_orphan_uploaded_videos


class Command(BaseCommand):
    help = _("Deletes any unused user uploaded video")

    def handle(self, *args, **options):
        delete_orphan_uploaded_videos()
