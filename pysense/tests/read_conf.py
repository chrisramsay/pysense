# -*- coding: utf-8 -*-
"""

"""
from __future__ import unicode_literals, print_function
import unittest
from yaml import load, dump
import os


class ReadConfTestCase(unittest.TestCase):
    def setUp(self):
        """
        The set up - parsed YAML
        """
        stream = open('{0}/files/config/test_two.yaml'.format(os.getcwd()))
        self._config = load(stream)

    def test_configs(self):
        print(self._config)
