"""
Initiates and builds a list of devices, holding their address, state and sensor type.
"""


class Devices(object):

    def __init__(self):
        self._address = None
        self._state = None
        self._type = None

    @property
    def address(self):
        """
        The I2C address of the device in question
        """
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the value of the address property
        """
        self._address = value

    @address.deleter
    def address(self):
        """
        Deletes the address property
        """
        del self._address
