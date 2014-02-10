# -*- coding: utf-8 -*-
"""
Initiates and builds a device, holding its address, state and sensor type.
"""
from __future__ import unicode_literals, print_function

import device.device_factory as dv
from device.devices import ir_thermo as irt

classes = {"irt": irt.IRThermo, "bar": irt.IRThermo}

dv.DeviceFactory(classes['irt']()).address()
dv.DeviceFactory(classes['irt']()).reading()
dv.DeviceFactory(classes['irt']()).state()
dv.DeviceFactory(classes['irt']()).type()

