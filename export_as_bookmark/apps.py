"""export_as_bookmark app definition."""

from django.apps import AppConfig
from django.conf import settings

from .redis import Redis


class ExportAsBookmarkConfig(AppConfig):  # type: ignore   # disallow_subclassing_any
    """export_as_bookmark app definition."""

    name = "export_as_bookmark"
    label = "export_as_bookmark"

    def ready(self) -> None:
        """Initialize app."""
        Redis.get_instance().ready(settings.EXPORT_AS_BOOKMARK_REDIS_URL)
        return
