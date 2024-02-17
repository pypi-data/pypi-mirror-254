from django.db import models

from wideo import get_video_model_string


class VideoField(models.ForeignKey):
    def __init__(self, *args, **kwargs):
        kwargs["to"] = get_video_model_string()
        kwargs["on_delete"] = models.SET_NULL if kwargs.get("null") else models.PROTECT
        super().__init__(*args, **kwargs)
