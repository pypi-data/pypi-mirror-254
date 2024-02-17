# -*- coding: utf-8 -*-
import json
from django.http import HttpRequest


def get_ip(request: HttpRequest) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_agent(request: HttpRequest) -> str:
    return request.META.get('HTTP_USER_AGENT', '')[:256]


def get_referer(request: HttpRequest) -> str:
    return request.META.get('HTTP_REFERER')


def get_full_url(request: HttpRequest) -> str:
    return request.build_absolute_uri()


def get_url_path(request: HttpRequest) -> str:
    return request.path


def get_host(request: HttpRequest) -> str:
    return '{}://{}'.format(request.scheme, request.META['HTTP_HOST'])


def get_form_data(request: HttpRequest) -> dict:
    return dict(request.POST.lists())


def get_json_data(request: HttpRequest) -> dict:
    return json.loads(request.body)


class RequestContentType:
    FormData = 'multipart/form-data'
    Json = 'application/json'


def get_request_data(request: HttpRequest) -> dict:
    if request.content_type == RequestContentType.FormData:
        return get_form_data(request)
    elif request.content_type == RequestContentType.Json:
        return get_json_data(request)
