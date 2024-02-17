# -*- coding: utf-8 -*-
import logging
import traceback
from django.conf import settings
from django.http import HttpRequest, Http404
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from dj3base import request as ru
from dj3base.exceptions.errors import Error, ErrorType, ServerUnknownError


def build_error_response(e: Error) -> JsonResponse:
    status_code = getattr(settings, "CLIENT_SIDE_ERROR_STATU_SCODE", 400)
    if e.error_type == ErrorType.ServerSideError:
        status_code = getattr(settings, "SERVER_SIDE_ERROR_STATU_SCODE", 400)

    rd = {
        'status': e.status,
        'error_message': e.message
    }
    if e.detail is not None:
        rd['detail'] = e.detail

    return JsonResponse(data=rd, status=status_code)


def log_error_message(logger: logging.Logger, request: HttpRequest, e: Error) -> str:
    if e.error_type == ErrorType.ServerSideError:
        error_message = f"\n" \
           f"ip: {ru.get_ip(request)}\n" + \
           f"url: {ru.get_full_url(request)}\n" + \
           f"content-type: {request.content_type}\n" + \
           f"request: {ru.get_request_data(request)}\n" + \
           f"message: {e.message}\n" + \
           f"cause: {e.cause}\n" + \
           f"traceback: {traceback.format_exc()}\n"
        logger.critical(error_message)
    else:
        error_message = f'[{request.path}]-[{e.status}]: {e.message}; {e.cause or ""}'
        logger.info(error_message)

    return error_message


class ErrorHandlingMiddleware(MiddlewareMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger(__name__)

    def process_exception(self, request: HttpRequest, exception: Exception):
        if isinstance(exception, Error):
            error_response = build_error_response(exception)
            log_error_message(self._logger, request, exception)
        elif isinstance(exception, Http404):
            # 内置错误, 内置处理
            raise exception
        else:
            exception = ServerUnknownError(cause=str(exception))
            error_response = build_error_response(exception)
            log_error_message(self._logger, request, exception)

        return error_response
