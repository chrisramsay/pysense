# -*- coding: utf-8 -*-
"""
Represents a concrete temperature value

Borrowed from http://www.stuffaboutcode.com/2013/12/raspberry-pi-python-temp-sensor-ds18b20.html
"""
from __future__ import unicode_literals, print_function


class Temperature():

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @property
    def centigrade(self):
        return float(self.raw_data) / 1000

    @property
    def fahrenheit(self):
        return round(self.centigrade * 9.0 / 5.0 + 23.0, 3)
