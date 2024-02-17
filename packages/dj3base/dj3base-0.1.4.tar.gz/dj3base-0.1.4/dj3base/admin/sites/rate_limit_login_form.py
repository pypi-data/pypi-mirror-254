# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from dj3base.request import get_ip


ADMIN_LOGIN_THROTTLE_PER_HOUR = 10


class RateLimitLoginForm(AuthenticationForm):
    ip2error_info = dict()
    throttle_per_hour = getattr(settings, 'ADMIN_LOGIN_THROTTLE_PER_HOUR', ADMIN_LOGIN_THROTTLE_PER_HOUR)

    def clean(self):
        # 清理过期统计
        for ip in list(self.ip2error_info.keys()):
            error_info = self.ip2error_info[ip]
            if error_info['expired_time'] < datetime.now():
                del self.ip2error_info[ip]

        # 检测IP异常数是否达到上限，如果受限，直接抛出相关异常
        ip = get_ip(self.request)
        error_info = self.ip2error_info.get(ip, None)
        if error_info is not None and error_info['count'] >= self.throttle_per_hour:
            raise ValidationError(
                "登录的次数已达上限，近期无法再登录！",
                code="invalid_login",
            )

        try:
            return super().clean()
        except ValidationError as e:
            # IP 异常数 + 1
            if error_info is None:
                error_info = {
                    'count': 1
                }
            else:
                error_info['count'] += 1
            error_info['expired_time'] = datetime.now() + timedelta(hours=1)
            self.ip2error_info[ip] = error_info
            raise e
