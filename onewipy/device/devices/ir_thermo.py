# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function

import abstract_device


# Concrete device:
class IRThermo(abstract_device.AbstractDevice):
    def __init__(self):
        pass

    def address(self):
        print('Getting address from {0}'.format(self.__class__))

    def reading(self):
        print('Getting reading from {0}'.format(self.__class__))

    def state(self):
        print('Getting state from {0}'.format(self.__class__))

    def type(self):
        print('Getting type from {0}'.format(self.__class__))
