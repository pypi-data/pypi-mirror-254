from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_video_model_string():
    """
    Get the dotted ``app.Model`` name for the video model as a string, just like
    ``get_image_model_string()`` from wagtailimages.
    """
    return getattr(settings, "WIDEO_VIDEO_MODEL", "wideo.Video")


def get_video_model():
    """
    Get the image model from the ``WAGTAILIMAGES_IMAGE_MODEL`` setting, just like
    ``get_image_model()`` from wagtailimages.
    """
    from django.apps import apps

    model_string = get_video_model_string()

    try:
        return apps.get_model(model_string, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "WIDEO_VIDEO_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "WIDEO_VIDEO_MODEL refers to model '%s' that has not been installed"
            % model_string
        )


def get_render_model_string():
    return getattr(settings, "WIDEO_RENDER_MODEL", "wideo.Render")


def get_render_model():
    from django.apps import apps

    model_string = get_render_model_string()

    try:
        return apps.get_model(model_string, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "WIDEO_RENDER_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "WIDEO_RENDER_MODEL refers to model '%s' that has not been installed"
            % model_string
        )
