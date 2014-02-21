# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import unittest

import pysense.device.reader
import pysense.device.device_factory


class DevicesTestCase(unittest.TestCase):
    def setUp(self):
        """
        The set up
        """
        device_conf = [{
            'type': 'CCT',
            'config': {
                'address': '28-000004d017ba', 'device_directory': u'tests/files/', 'type': u'?'
            },
        }, {
            'type': 'IRT',
            'config': {
                'address': '28-000004ce67e3', 'type': u'?'
            },
        }, ]
        self.r = pysense.device.reader.Reader(device_conf)

    def test_cct(self):
        # Check that r is an instance of Reader
        self.assertIsInstance(self.r, pysense.device.reader.Reader)
        # Check that first device is an instance of DeviceFactory
        dev_one = self.r.devs[0]
        self.assertIsInstance(dev_one, pysense.device.device_factory.DeviceFactory)
        # Check that address is as set
        self.assertEqual(dev_one.address(), '28-000004d017ba')

    def test_irt(self):
        # Check that r is an instance of Reader
        self.assertIsInstance(self.r, pysense.device.reader.Reader)
        # Check that first device is an instance of DeviceFactory
        dev_two = self.r.devs[1]
        self.assertIsInstance(dev_two, pysense.device.device_factory.DeviceFactory)
        # Check that address is as set
        self.assertEqual(dev_two.address(), '28-000004ce67e3')

if __name__ == '__main__':
    unittest.main()
