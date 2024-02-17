# -*- coding: utf-8 -*-
from django.http import JsonResponse


def build_success_response(data: dict = None):
    success_result = {
        'status': 'OK'
    }

    if data is not None:
        success_result['data'] = data
    return JsonResponse(data=success_result)
