from django.forms import FileInput


class VideoUploadWidget(FileInput):
    template_name = f"{__package__}/forms/file.html"
