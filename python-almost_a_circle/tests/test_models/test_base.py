#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_auto_id_assignment(self):
        """Test automatic ID assignment"""
        # Create multiple Base instances without passing IDs
        base1 = Base()
        base2 = Base()
        base3 = Base()

        # Check if the IDs are automatically assigned starting from 1
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_auto_id_assignment(self):
        """Test automatic ID assignment"""
        # Create multiple Base instances without passing IDs
        base1 = Base()
        base2 = Base()
        base3 = Base()

        # Check if the IDs are automatically assigned starting from 1
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

   


    def test_to_json_string(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertTrue(isinstance(json_string, str))

    def test_to_json_string_content(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertCountEqual(json.loads(json_string), dictionary)

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        json_list = Base.from_json_string(string)
        self.assertTrue(isinstance(json_list, list))

    def test_from_json_string_content(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        expected_list = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_list = Base.from_json_string(string)
        self.assertEqual(json_list, expected_list)

    def test_from_json_string_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])
