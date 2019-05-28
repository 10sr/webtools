# from pprint import pformat

from django.conf import settings
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseRedirect,
)
from django.template import loader
from django.urls import reverse

from .redis import Redis


def index(req: HttpRequest) -> HttpResponse:
    tpl = loader.get_template("export_as_bookmark/index.html.dtl")
    return HttpResponse(tpl.render({}, req))


def post(req: HttpRequest) -> HttpResponse:
    try:
        body = req.POST["body"]
    except KeyError:
        return HttpResponseBadRequest("Body not given")

    print(body)
    redis = Redis(settings)
    redis.set("1", body)
    return HttpResponseRedirect(reverse("export_as_bookmark:download", args=("1",)))


def download(req: HttpRequest, id: str) -> HttpResponse:
    redis = Redis(settings)
    return HttpResponse(f"{id}: {repr(redis.get(id))}")
