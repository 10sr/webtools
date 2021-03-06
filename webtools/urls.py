"""webtools URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

_path = "webtools"

urlpatterns = [
    path("", RedirectView.as_view(url=f"/{_path}/")),
    path(f"{_path}/export-as-bookmark/", include("export_as_bookmark.urls")),
    path(f"{_path}/lggr/", include("lggr.urls")),
    path(f"{_path}/admin/", admin.site.urls),
    path(f"{_path}/admin/doc/", include("django.contrib.admindocs.urls")),
    path(f"{_path}/", include("webtools.rootapp.urls")),
]
