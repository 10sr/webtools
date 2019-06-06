import pprint
import logging

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseRedirect,
)


logger = logging.getLogger(__name__)

# Create your views here.

def get(req: HttpRequest) -> HttpResponse:
    request_id = id(req)
    logger.warning(f"Id: {request_id} get/ Requested >>>>>")
    logger.warning(f"Id: {request_id} req.META:")
    logger.warning(f"Id: {request_id} {pprint.pformat(req.META)}")
    logger.warning(f"Id: {request_id} req.GET:")
    logger.warning(f"Id: {request_id} {pprint.pformat(req.GET.dict())}")
    logger.warning(f"Id: {request_id} get/ Requested <<<<<")
    return HttpResponse("")

def post(req: HttpRequest) -> HttpResponse:
    logger.warning("Requested")
    return HttpResponse("")
