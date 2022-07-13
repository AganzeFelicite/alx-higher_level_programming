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
    def test_to_json_string_None_list(self):
        s = Base.to_json_string(None)
        self.assertEqual("[]", s)

    def test_to_json_string_empty_list(self):
        s = Base.to_json_string([])
        self.assertEqual("[]", s)

    def test_to_json_string_single_item(self):
        s = Base.to_json_string([{'id': 2,'width': 4, 'height': 3}])
        self.assertEqual('[{"id": 2, "width": 4, "height": 3}]', s)

    def test_to_json_string_multiple_items(self):
        s = Base.to_json_string(
            [{'id':2,'width': 4, 'height':3}, {'id':2,'width': 4, 'height':3}])
        self.assertEqual(
            '[{"id": 2, "width": 4, "height": 3}, {"id": 2, "width": 4, "height": 3}]', s)

    def test_from_json_string_empty_input(self):
        l = Base.from_json_string("")
        self.assertEqual([], l)
    
    def test_from_json_string_None_input(self):
        l = Base.from_json_string(None)
        self.assertEqual([], l)

    def test_from_json_string_ok_input(self):
        l = Base.from_json_string(
            '[{"id": 2, "width": 4, "height": 3}, {"id": 2, "width": 4, "height": 3}]')
        expected = [{'id':2,'width': 4, 'height':3}, {'id':2,'width': 4, 'height':3}]
        self.assertEqual(expected, l)
