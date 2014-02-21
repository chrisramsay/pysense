# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import unittest
from yaml import load, dump
import os


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        """
        The set up
        """
        self.device_conf = [{
            'type': 'CCT',
            'config': {
                'address': '8-000004bfccc8', 'device_directory': u'/sys/bus/w1/devices/',
            },
        }, {
            'type': 'IRT',
            'config': {
                'address': '28-000004ce67e3',
            },
        }, ]

    def test_dump(self):
        pass #print(dump(self.device_conf))

    def test_load(self):
        """
        Asserts that the example_one.yaml is same format as that set up in set up.
        """
        stream = open('{0}/files/config/test_one.yaml'.format(os.getcwd()))
        output = load(stream)
        self.assertEqual(output, self.device_conf)
