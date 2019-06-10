# from pprint import pformat
import html

from hashlib import sha512

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.template import loader
from django.urls import reverse

from .bookmark_exporter import BookmarkExporter
from .redis import Redis


def index(req: HttpRequest) -> HttpResponse:
    tpl = loader.get_template("export_as_bookmark/index.html.dtl")
    return HttpResponse(tpl.render({}, req))


def post(req: HttpRequest) -> HttpResponse:
    try:
        body = req.POST["body"]
    except KeyError:
        return HttpResponseBadRequest("Body not given")

    request_id = id(req)
    name = f"ExportAsBookmark-{request_id}"
    exporter = BookmarkExporter.from_lines(body)
    exported_bytes = exporter.export(name).encode("utf-8")
    key = sha512(exported_bytes).hexdigest()
    Redis.set(key, exported_bytes, ex=60)
    return HttpResponseRedirect(reverse("export_as_bookmark:done", args=(key, name)))


def done(req: HttpRequest, id: str, name: str) -> HttpResponse:
    tpl = loader.get_template("export_as_bookmark/done.html.dtl")
    # TODO: Show expire limit
    return HttpResponse(tpl.render({"id": id, "name": name}, req))


def download(req: HttpRequest, id: str, name: str) -> HttpResponse:
    # TODO: Use req.session?
    # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.session
    val = Redis.get(id)
    if val is None:
        return HttpResponseNotFound(f"Content of id {id[:24]} not found. Expired?")
    res = HttpResponse(val.decode("utf-8"))
    res["Referrer-Policy"] = "origin"
    return res
