from typing import Any

from django.template.defaulttags import register


@register.simple_tag
def settings(name: str, default: Any = None) -> Any:
    from django.conf import settings

    return getattr(settings, name, default)
