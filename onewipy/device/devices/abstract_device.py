# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function


# The abstract device:
class AbstractDevice:

    def __init__(self, device_config):
        self._address = device_config['address']
        self._reading = device_config['reading']
        self._state = device_config['state']
        self._type = device_config['type']

    @property
    def address(self):
        return self._address

    @property
    def reading(self):
        pass

    @property
    def state(self):
        pass

    @property
    def type(self):
        pass
