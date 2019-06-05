from django.apps import AppConfig
from django.conf import settings


class ExportAsBookmarkConfig(AppConfig):
    name = "export_as_bookmark"
    label = "export_as_bookmark"

    def ready(self):
        from .redis import Redis
        Redis.ready(settings)
        return
