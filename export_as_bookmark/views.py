# from pprint import pformat

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
    Redis.set("1", body.encode("utf-8"), ex=60)
    return HttpResponseRedirect(reverse("export_as_bookmark:download", args=("1",)))


def download(req: HttpRequest, id: str) -> HttpResponse:
    val = Redis.get(id)
    if val:
        val = val.decode("utf-8")
    return HttpResponse(f"{id}: {repr(val)}")
