from django.apps import AppConfig
from django.conf import settings


class ExportAsBookmarkConfig(AppConfig):  # type: ignore   # disallow_subclassing_any
    name = "export_as_bookmark"
    label = "export_as_bookmark"

    def ready(self) -> None:
        from .redis import Redis

        Redis.ready(settings.EXPORT_AS_BOOKMARK_REDIS_URL)
        return
