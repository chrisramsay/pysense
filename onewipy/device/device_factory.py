# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
# import devices.ir_thermo


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

#DeviceFactory(devices.ir_thermo.IRThermo()).address()
#DeviceFactory(devices.ir_thermo.IRThermo()).reading()
#DeviceFactory(devices.ir_thermo.IRThermo()).state()
#DeviceFactory(devices.ir_thermo.IRThermo()).type()
