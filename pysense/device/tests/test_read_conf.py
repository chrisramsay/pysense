# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import os
import unittest

from yaml import load, dump

import pysense.device.reader
from pysense.util.temperature import Temperature


class ReadConfTestCase(unittest.TestCase):
    def setUp(self):
        """
        The set up - parsed YAML
        """
        stream = open('{0}/tests/files/config/test_two.yaml'.format(os.getcwd()))
        self._config = load(stream)

    def test_configs(self):
        test_conf = [
            {'config':
                {'device_directory': 'files/', 'address': '28-000004bfccc8'},
             'type': 'CCT'
            },
            {'config':
                {'device_directory': 'files/', 'address': '28-000004d017ba'},
             'type': 'CCT'
            },
            {'config':
                {'address': '28-000004ce67e3'},
             'type': 'IRT'
            }
        ]
        self.assertEqual(self._config, test_conf)

    def test_load_config(self):
        reader = pysense.device.reader.Reader(self._config)
        devices = reader.devices()
        # CCT 1
        cct_one = devices.next()
        self.assertIsInstance(cct_one.reading(), Temperature)
        self.assertEqual(cct_one.reading().centigrade, 15.062)
        self.assertEqual(cct_one.reading().fahrenheit, 50.112)
        # CCT 2
        cct_two = devices.next()
        self.assertIsInstance(cct_two.reading(), Temperature)
        self.assertEqual(cct_two.reading().centigrade, 24.437)
        self.assertEqual(cct_two.reading().fahrenheit, 66.987)
