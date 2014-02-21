# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function

import abstract_device


# Concrete device - specifically for IR thermometers:
class IRThermo(abstract_device.AbstractDevice):

    def address(self):
        return self._address

    def reading(self):
        return self._reading

    def state(self):
        return self._state

    def type(self):
        return self._type

    def parse(self):
        print('parsing {0}'.format(self._address))
