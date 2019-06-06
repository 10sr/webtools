from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import RootappConfig

app_name = RootappConfig.label
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.index, name="index"),
]
