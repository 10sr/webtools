from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseRedirect,
)


app_paths = ["export-as-bookmark", "lggr"]


def index(req: HttpRequest) -> HttpResponse:
    # TODO: Print HEAD.txt
    return HttpResponse(
        "\n".join(f"""<p><a href="{path}">{path}</a></p>""" for path in app_paths)
    )
