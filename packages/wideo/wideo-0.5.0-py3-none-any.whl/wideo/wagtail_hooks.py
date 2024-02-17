from django.urls import include, path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from . import admin_urls


@hooks.register("register_icons")
def register_icons(icons: list[str]) -> list[str]:
    return icons + [f"{__package__}/icons/video.svg"]


@hooks.register("register_admin_urls")
def register_admin_urls() -> list:
    return [
        path(f"{__package__}/", include(admin_urls, namespace="wideo")),
    ]


@hooks.register("register_admin_menu_item")
def register_videos_menu_item() -> MenuItem:
    return MenuItem("Videos", reverse("wideo:index"), icon_name="video")
