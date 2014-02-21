# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import unittest
import os

import pysense.device.reader
import pysense.device.device_factory
from pysense.util.temperature import Temperature


class ReaderTestCase(unittest.TestCase):
    def setUp(self):
        """
        The set up - a typical config
        """
        device_conf = [{
            'type': 'CCT',
            'config': {
                'address': '28-000004bfccc8', 'device_directory': u'{0}/files/'.format(os.path.abspath(__file__)[:-15]), 'type': u'?'
            },
        }, {
            'type': 'IRT',
            'config': {
                'address': '28-000004ce67e3', 'type': u'?'
            },
        }, ]
        # Start instance of Reader with a config
        self.reader = pysense.device.reader.Reader(device_conf)

    def test_cct(self):
        # Check that r is an instance of Reader
        self.assertIsInstance(self.reader, pysense.device.reader.Reader)
        # Check that first device is an instance of DeviceFactory
        dev_one = self.reader.device_list[0]
        self.assertIsInstance(dev_one, pysense.device.device_factory.DeviceFactory)
        # Check that address is as set
        self.assertEqual(dev_one.address(), '28-000004bfccc8')

    def test_irt(self):
        # Check that r is an instance of Reader
        self.assertIsInstance(self.reader, pysense.device.reader.Reader)
        # Check that second device is an instance of DeviceFactory
        dev_two = self.reader.device_list[1]
        self.assertIsInstance(dev_two, pysense.device.device_factory.DeviceFactory)
        # Check that address is as set
        self.assertEqual(dev_two.address(), '28-000004ce67e3')

    def test_generate(self):
        device_gen = self.reader.devices()
        # Check that first device is an instance of DeviceFactory
        self.assertIsInstance(device_gen.next(), pysense.device.device_factory.DeviceFactory)
        # Check that second device is an instance of DeviceFactory
        self.assertIsInstance(device_gen.next(), pysense.device.device_factory.DeviceFactory)
        # Assert that we get to the end of the list
        self.assertRaises(StopIteration, lambda: device_gen.next())

    def test_cct_reading(self):
        # Get the chosen device
        dev_cct = self.reader.device_list[0]
        # Take a reading
        reading = dev_cct.reading()
        # Check that instance is Temperature
        self.assertIsInstance(reading, Temperature)
        # Assert that the temperature is measured at 15.062 Centigrade
        self.assertEqual(reading.centigrade, 15.062)
        # Assert that the temperature is measured at 50.112 Fahrenheit
        self.assertEqual(reading.fahrenheit, 50.112)

if __name__ == '__main__':
    unittest.main()
