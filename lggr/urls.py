from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import LggrConfig

app_name = LggrConfig.label
urlpatterns = [
    # path("", views.index, name="index"),
    path("get", views.get, name="get"),
    path("post", views.post, name="post"),
    path("", RedirectView.as_view(url=f"get")),
]
