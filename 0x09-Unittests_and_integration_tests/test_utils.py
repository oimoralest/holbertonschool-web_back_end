#!/usr/bin/env python3
"""Writing unit and integration test with Python"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """unit test is the first
    step in TDD"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test a function using pattern parameterized"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, expected):
        """ test assertion raises from exceptions
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, expected)


class TestGetJson(unittest.TestCase):
    """ getting started working with mock testing
        mock some class or object is important to save resources
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ mock testing to test http GET requests
        Args:
            test_url ([type]): [description]
            test_payload ([type]): [description]
        """
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test Memoize class
    Args:
        unittest ([type]): [description]
    """

    def test_memoize(self):
        """ test class memoization
        Args:
            unittest ([type]): [description]
        """
        class TestClass:
            """ Test Memoize class
            Args:
                unittest ([type]): [description]
            """

            def a_method(self):
                """ Method return a int
                """
                return 42

            @memoize
            def a_property(self):
                """ method call a method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            my_instance = TestClass()
            value = my_instance.a_property
            value = my_instance.a_property
            self.assertEqual(value, 42)
            mock.method()
            mock.method.assert_called_once()
            mock.assert_called_once()
