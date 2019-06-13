"""App definitiion for webtools roopapp."""


from django.apps import AppConfig


class RootappConfig(AppConfig):  # type: ignore   # disallow_subclassing_any
    """Webtools rootapp definition."""

    name = "webtools.rootapp"
    label = "rootapp"
