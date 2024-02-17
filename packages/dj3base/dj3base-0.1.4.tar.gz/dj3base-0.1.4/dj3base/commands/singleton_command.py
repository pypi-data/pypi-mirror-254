# -*- coding: utf-8 -*-
import sys
import os
from abc import ABC

from django.core.management.base import BaseCommand
from tendo import singleton


class SingletonCommand(BaseCommand, ABC):
    related_env = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        flavor_id = ''
        if self.related_env is not None:
            flavor_id = os.environ.get(self.related_env, '')

        try:
            self._single_instance = singleton.SingleInstance(flavor_id)
        except singleton.SingleInstanceException:
            sys.exit(-2)
