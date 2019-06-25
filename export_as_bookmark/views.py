"""View definitions of export_as_bookmark."""


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
    """
    Return index.

    :param req: Request object
    :returns: Index page
    """
    tpl = loader.get_template("export_as_bookmark/index.html.dtl")
    return HttpResponse(tpl.render({}, req))


def post(req: HttpRequest) -> HttpResponse:
    """
    Receive post request and redirect to download page.

    :param req: Request object
    :returns: Redirect to done page
    """
    try:
        body = req.POST["body"]
    except KeyError:
        return HttpResponseBadRequest("Body not given")

    redis = Redis.get_instance()

    request_id = id(req)
    name = f"ExportAsBookmark-{request_id}"
    exporter = BookmarkExporter.from_lines(body)
    exported_bytes = exporter.export(name).encode("utf-8")
    key = sha512(exported_bytes).hexdigest()
    redis.set(key, exported_bytes, ex=60)
    return HttpResponseRedirect(reverse("export_as_bookmark:done", args=(key, name)))


def done(req: HttpRequest, id: str, name: str) -> HttpResponse:
    """
    Return link to download exported html file.

    :param req: Request object
    :param id: Result id
    :param name: Bookmark name
    :returns: Download page
    """
    tpl = loader.get_template("export_as_bookmark/done.html.dtl")
    # TODO: Show expire limit
    return HttpResponse(tpl.render({"id": id, "name": name}, req))


def download(req: HttpRequest, id: str, name: str) -> HttpResponse:
    """
    Return exported bookmark content.

    :param req: Request object
    :param id: Result id
    :param name: Bookmark name
    :return: Exported html content
    """
    # TODO: Use req.session?
    # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.session
    redis = Redis.get_instance()

    val = redis.get(id)
    if val is None:
        return HttpResponseNotFound(f"Content of id {id[:24]} not found. Expired?")
    res = HttpResponse(val.decode("utf-8"))
    res["Referrer-Policy"] = "origin"
    return res
