from django import forms

from .models import Video
from .widgets import VideoUploadWidget


class BaseVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "upload", "tags"]


class VideoForm(BaseVideoForm):
    class Meta(BaseVideoForm.Meta):
        widgets = {"upload": VideoUploadWidget()}
