# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function


class Temperature():

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @property
    def Centigrade(self):
        return float(self.raw_data) / 1000

    @property
    def Fahrenheit(self):
        return self.C * 9.0 / 5.0 + 23.0
