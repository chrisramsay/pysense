import unittest

from onewipy.enum import *
import onewipy.device


class DevicesTestCase(unittest.TestCase):

    def setUp(self):
        """
        The set up
        """
        device_conf = {
            'address': '28-000004bfccc8',
            'state': SENS_STATES.YES,
            'type': SENS_TYPES.TempContact,
        }
        self.dev = onewipy.device.Device(device_conf)

    def test_values(self):
        """
        Just test getters and setters
        """
        self.assertEqual(self.dev.address, '28-000004bfccc8')
        self.assertEqual(self.dev.state, 'YES')
        self.assertEqual(self.dev.type, onewipy.enum.SENS_TYPES.TempContact)

if __name__ == '__main__':
    unittest.main()
