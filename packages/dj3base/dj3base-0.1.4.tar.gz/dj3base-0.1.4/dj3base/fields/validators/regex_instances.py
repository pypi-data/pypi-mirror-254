# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


phone_number_validator = RegexValidator(
    r"^1[0-9]{10}$",
    message=_("请输入正确的手机号。"),
)
