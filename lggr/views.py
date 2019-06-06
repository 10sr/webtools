import pprint
import logging

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseRedirect,
)
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)

def get(req: HttpRequest) -> HttpResponse:
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
    logger.warning(log)
    return HttpResponse(log, content_type="text/plain")

# curl -X POST -d @a.txt localhost:7700/webtools/lggr/post
@csrf_exempt
def post(req: HttpRequest) -> HttpResponse:
    request_id = id(req)
    log = f"""Id: {request_id} post/ Requested >>>>>
req.META:
{pprint.pformat(req.META)}
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
