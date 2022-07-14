#!/usr/bin/python3
"""this is the test cases of the the Base module"""


import unittest
from models.base import Base


class BaseModuleTest(unittest.TestCase):
    '''test for none'''

    def test_none(self):
        b = Base()
        self.assertEqual(1, b.id)

    '''test when it is provided'''
    def test_provided(self):
        b = Base(3)
        self.assertEqual(3, b.id) 
