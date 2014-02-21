# -*- coding: utf-8 -*-
"""
Passes through commands to the created device.
"""
from __future__ import unicode_literals, print_function


class DeviceFactory:

    def __init__(self, factory):
        self.factory = factory

    def address(self):
        return self.factory.address()

    def reading(self):
        return self.factory.reading()

    def state(self):
        return self.factory.state()

    def type(self):
        return self.factory.type()

