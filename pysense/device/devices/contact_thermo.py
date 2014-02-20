# -*- coding: utf-8 -*-
"""
This is a concrete implementation of the device abstract base class for the DS18B20 contact thermometer.

It requires some extra configuration options:



The output from this sensor looks like this:

    f6 01 4b 46 7f ff 0a 10 eb : crc=eb YES
    f6 01 4b 46 7f ff 0a 10 eb t=31375

It will report as a device at (for example):

    /sys/bus/w1/devices/28-000004ce67e3/

With the data in the w1_slave file of the above directory

"""
from __future__ import unicode_literals, print_function

import abstract_device
from pysense.util.temperature import Temperature


class ContactThermo(abstract_device.AbstractDevice):

    def __init__(self, device_config):
        super(ContactThermo, self).__init__(device_config)
        self._device_directory = device_config['device_directory']
        self.sensor_file = self._device_directory + self._address + '/w1_slave'

    def address(self):
        print('Getting address from {0}: {1}, slightly differently'.format(self.__class__, self._address))

    def reading(self):
        self._reading = 12903
        self._reading = Temperature(self._reading)
        print('Getting reading from {0}: {1}, slightly differently'.format(self.__class__, self._reading.Centigrade))

    def state(self):
        print('Getting state from {0}: {1}, slightly differently'.format(self.__class__, self._state))

    def type(self):
        print('Getting type from {0}: {1}, slightly differently'.format(self.__class__, self._type))

    def get_loc(self):
        print('Getting type from {0}: {1}, slightly differently'.format(self.__class__, self._device_directory))

    def parse(self):
        print(self.sensor_file)

    def _read_file(self):
        sensor_file = open(self.sensor_file, "r")
        lines = sensor_file.readlines()
        sensor_file.close()
        return lines

    def _update_temp(self):
        data = self._read_file()
        if data[0].strip()[-3:] == "YES":
            equals_pos = data[1].find("t=")
            if equals_pos != -1:
                temp_data = data[1][equals_pos+2:]
