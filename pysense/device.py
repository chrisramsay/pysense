# -*- coding: utf-8 -*-
"""
Initiates and builds a device, holding its address, state and sensor type.
"""
from __future__ import unicode_literals, print_function

import device.device_factory as dv
from device.devices import ir_thermo as irt
from device.devices import contact_thermo as ctt

classes = {"irt": irt.IRThermo, "ctt": ctt.ContactThermo}

device_conf_1 = {
    'address': '28-000004bfccc8',
    'reading': u'10.187˚C',
    'state': 'YES',
    'type': u'?',
}

device_conf_2 = {
    'address': '28-000004d017ba',
    'reading': u'11.937˚C',
    'state': 'YES',
    'type': u'?',
}

my_irt = classes['irt'](device_conf_1)

print(my_irt)
print(dv.DeviceFactory(my_irt))

#dv.DeviceFactory(my_irt).address()
#dv.DeviceFactory(my_irt).reading()
#dv.DeviceFactory(my_irt).state()
#dv.DeviceFactory(my_irt).type()

#my_ctt = classes['ctt'](device_conf_2)

#dv.DeviceFactory(my_ctt).address()
#dv.DeviceFactory(my_ctt).reading()
#dv.DeviceFactory(my_ctt).state()
#dv.DeviceFactory(my_ctt).type()

