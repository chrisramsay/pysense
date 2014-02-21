# -*- coding: utf-8 -*-
"""
Initiates and builds all devices, holding its address, state and sensor type.
"""
from __future__ import unicode_literals, print_function

import device_factory as dv
from devices import ir_thermo as irt
from devices import contact_thermo as ctt


DEVICE_CLASSES = dict(IRT=irt.IRThermo, CCT=ctt.ContactThermo)


class Reader(object):

    def __init__(self, device_config):
        """
        For each device, set up the class and then do device specific stuff
        """
        self.device_list = []
        for dev in device_config:
            my_irt = DEVICE_CLASSES[dev['type']](dev['config'])
            self.device_list.append(dv.DeviceFactory(my_irt))

    def get_device_list(self):
        return self.device_list

    def devices(self):
        for dev in self.device_list:
            yield dev
