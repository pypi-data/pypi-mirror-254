# -*- coding: utf-8 -*-
import sys


_IS_UNIT_TESTING = sys.argv[1:2] == ['test']


def is_unit_testing() -> bool:
    return _IS_UNIT_TESTING
