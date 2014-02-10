# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function


# The abstract device:
class AbstractDevice:

    @property
    def address(self):
        pass

    @property
    def reading(self):
        pass

    @property
    def state(self):
        pass

    @property
    def type(self):
        pass
