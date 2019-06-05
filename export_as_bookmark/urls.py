from django.urls import path

from . import views
from .apps import ExportAsBookmarkConfig

app_name = ExportAsBookmarkConfig.label
urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.post, name="post"),
    path("done/<id>/<name>", views.done, name="done"),
    path("download/<id>/<name>.html", views.download, name="download"),
]
