"""
Initiates and builds a device, holding its address, state and sensor type.
"""


class Device(object):

    def __init__(self, device_conf):
        """
        """
        self._address = device_conf['address']
        self._state = device_conf['state']
        self._type = device_conf['type']

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @address.deleter
    def address(self):
        del self._address

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @state.deleter
    def state(self):
        del self._state

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @type.deleter
    def type(self):
        del self._type
