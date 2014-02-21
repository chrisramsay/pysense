# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
from abc import ABCMeta, abstractmethod, abstractproperty


# The abstract device:
class AbstractDevice:

    __metaclass__ = ABCMeta

    def __init__(self, device_config):
        self._address = device_config['address']
        self._type = device_config['type']

    @abstractproperty
    def address(self):
        pass

    @abstractproperty
    def reading(self):
        pass

    @abstractproperty
    def state(self):
        pass

    @abstractproperty
    def type(self):
        pass

