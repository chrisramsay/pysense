# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function

import abstract_device


# Concrete device - specifically for contact thermometers:
class ContactThermo(abstract_device.AbstractDevice):

    def address(self):
        print('Getting address from {0}: {1}, slightly differently'.format(self.__class__, self._address))

    def reading(self):
        print('Getting reading from {0}: {1}, slightly differently'.format(self.__class__, self._reading))

    def state(self):
        print('Getting state from {0}: {1}, slightly differently'.format(self.__class__, self._state))

    def type(self):
        print('Getting type from {0}: {1}, slightly differently'.format(self.__class__, self._type))
