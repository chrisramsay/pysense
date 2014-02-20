# -*- coding: utf-8 -*-
"""
Passes through commands to the created device.
"""
from __future__ import unicode_literals, print_function


class DeviceFactory:

    def __init__(self, factory):
        self.factory = factory

    def address(self):
        self.factory.address()

    def reading(self):
        self.factory.reading()

    def state(self):
        self.factory.state()

    def type(self):
        self.factory.type()

    def parse(self):
        self.factory.parse()
