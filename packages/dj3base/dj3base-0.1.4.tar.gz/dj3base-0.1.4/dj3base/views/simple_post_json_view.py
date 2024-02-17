# -*- coding: utf-8 -*-
import abc
import json

from django.views.generic import View
from django.http import FileResponse
from dj3base.exceptions.errors import ServerKnownError
from dj3base.views.utils import build_success_response


class SimplePostJsonView(View):

    def post(self, *_, **__):
        request_data = json.loads(self.request.body)
        result = self.handle_post(request_data)
        if result is None:
            return build_success_response()
        elif isinstance(result, dict):
            return build_success_response(result)
        elif isinstance(result, FileResponse):
            return result
        else:
            raise ServerKnownError(cause=f"handle_post返回值类型未知: {type(result).__name__}")

    @abc.abstractmethod
    def handle_post(self, request_data: dict):
        raise NotImplementedError()
