from django.apps import AppConfig


class RootappConfig(AppConfig):  # type: ignore   # disallow_subclassing_any
    name = "webtools.rootapp"
    label = "rootapp"
