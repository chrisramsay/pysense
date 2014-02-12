# -*- coding: utf-8 -*-
"""
This is a concrete implementation of the device abstract base class for the DS18B20 contact thermometer.

The output from this sensor looks like this:

    f6 01 4b 46 7f ff 0a 10 eb : crc=eb YES
    f6 01 4b 46 7f ff 0a 10 eb t=31375

It will report as a device at (for example):

    /sys/bus/w1/devices/28-000004ce67e3/

With the data in the w1_slave file of the above directory

"""
from __future__ import unicode_literals, print_function

import abstract_device


class ContactThermo(abstract_device.AbstractDevice):

    def address(self):
        print('Getting address from {0}: {1}, slightly differently'.format(self.__class__, self._address))

    def reading(self):
        print('Getting reading from {0}: {1}, slightly differently'.format(self.__class__, self._reading))

    def state(self):
        print('Getting state from {0}: {1}, slightly differently'.format(self.__class__, self._state))

    def type(self):
        print('Getting type from {0}: {1}, slightly differently'.format(self.__class__, self._type))
