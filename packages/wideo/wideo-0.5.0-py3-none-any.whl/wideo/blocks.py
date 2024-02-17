from wagtail.blocks import BooleanBlock, StructBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from wideo import get_video_model_string


class VideoBlock(StructBlock):
    video = SnippetChooserBlock(target_model=get_video_model_string())
    autoplay = BooleanBlock(required=False)
    controls = BooleanBlock(required=False)
    muted = BooleanBlock(required=False)

    class Meta:
        label = "Video"
        template = "wideo/blocks/video.html"
