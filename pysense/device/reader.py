# -*- coding: utf-8 -*-
"""
Initiates and builds all devices, holding its address, state and sensor type.
"""
from __future__ import unicode_literals, print_function

import device_factory as dv
from devices import ir_thermo as irt
from devices import contact_thermo as ctt


DEVICE_CLASSES = {'IRT': irt.IRThermo, 'CCT': ctt.ContactThermo}


class Reader(object):

    def __init__(self, device_config):
        """
        For each device, set up the class and then do device specific stuff
        """
        self.devs = []
        for dev in device_config:
            my_irt = DEVICE_CLASSES[dev['type']](dev['config'])
            self.devs.append(dv.DeviceFactory(my_irt))

    def get_devs(self):
        return self.devs
