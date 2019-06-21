"""Views for webtools rootapp."""

from django.conf import settings
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseRedirect,
)

app_paths = ["export-as-bookmark", "lggr"]


def index(req: HttpRequest) -> HttpResponse:
    """
    Return index page.

    :param req: Request object
    :returns: Root index page
    """
    # TODO: Print HEAD.txt
    return HttpResponse(
        "\n".join(f"""<p><a href="{path}">{path}</a></p>""" for path in app_paths)
        +
        # TODO: Escape revisiion
        """<p><a href="{url}">Webtools<a/> Revision: {rev}</p>""".format(
            url="https://github.com/10sr/webtools",
            rev=settings.WEBTOOLS_REVISION or "Unavailable",
        )
    )
