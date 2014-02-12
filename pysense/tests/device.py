# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import unittest

from pysense.enum import *
import pysense.device


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
        self.dev = pysense.device.Device(device_conf)

    def test_values(self):
        """
        Just test getters and setters
        """
        self.assertEqual(self.dev.address, '28-000004bfccc8')
        self.assertEqual(self.dev.state, 'YES')
        self.assertEqual(self.dev.type, pysense.enum.SENS_TYPES.TempContact)

if __name__ == '__main__':
    unittest.main()
