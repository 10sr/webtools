"""View definitions of lggr app."""

import logging
import pprint

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.template import loader
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from ratelimit.decorators import ratelimit

logger = logging.getLogger(__name__)


def index(req: HttpRequest) -> HttpResponse:
    """Return page to test some requests.

    :param req: Request object
    :returns: Test page
    """
    tpl = loader.get_template("lggr/index.html.dtl")
    # https://stackoverflow.com/questions/4591525/is-it-possible-to-pass-query-parameters-via-djangos-url-template-tag
    return HttpResponse(tpl.render({"v1": "value1", "v2": str(timezone.now())}, req))


def get(req: HttpRequest) -> HttpResponse:
    """Log get requests.

    :param req: Request object
    :returns: Get log
    """
    request_id = id(req)
    log = f"""Id: {request_id} get/ Requested >>>>>
req.META:
{pprint.pformat(req.META)}
req.GET:
{pprint.pformat(req.GET.dict())}
Id: {request_id} get/ Requested <<<<<
"""
    # logger.warning(f"Id: {request_id} get/ Requested >>>>>")
    # logger.warning(f"Id: {request_id} req.META:")
    # logger.warning(f"Id: {request_id} {pprint.pformat(req.META)}")
    # logger.warning(f"Id: {request_id} req.GET:")
    # logger.warning(f"Id: {request_id} {pprint.pformat(req.GET.dict())}")
    # logger.warning(f"Id: {request_id} get/ Requested <<<<<")
    # TODO: Any other way of logging other than warning?
    logger.warning(log)
    return HttpResponse(log, content_type="text/plain")


# curl -X POST -d @a.txt localhost:7700/webtools/lggr/post
# TODO: Possible to change key via config?
@ratelimit(  # type: ignore   # disallow_untyped_decorators
    key="header:x-real-ip", rate="1/s", method=ratelimit.UNSAFE, block=True
)
@csrf_exempt  # type: ignore   # disallow_untyped_decorators
def post(req: HttpRequest) -> HttpResponse:
    """Log post requests.

    :param req: Request object
    :returns: Post log
    """
    request_id = id(req)
    log = f"""Id: {request_id} post/ Requested >>>>>
req.META:
{pprint.pformat(req.META)}
req.GET:
{pprint.pformat(req.GET.dict())}
req.body:
{repr(req.body)}
req.POST:
{pprint.pformat(req.POST.dict())}
Id: {request_id} post/ Requested <<<<<
"""
    # logger.warning(f"Id: {request_id} post/ Requested >>>>>")
    # logger.warning(f"Id: {request_id} req.META:")
    # logger.warning(f"Id: {request_id} {pprint.pformat(req.META)}")
    # logger.warning(f"Id: {request_id} req.body:")
    # logger.warning(f"Id: {request_id} {repr(req.body)}")
    # logger.warning(f"Id: {request_id} req.POST:")
    # logger.warning(f"Id: {request_id} {pprint.pformat(req.POST.dict())}")
    # logger.warning(f"Id: {request_id} post/ Requested <<<<<")
    logger.warning(log)
    return HttpResponse(log, content_type="text/plain")
