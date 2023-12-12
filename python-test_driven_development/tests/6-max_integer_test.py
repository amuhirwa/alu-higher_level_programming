#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max integer function"""
    def test_max_integer(self):
        items = [1, 2, 4, 5, 3]
        self.assertEqual(max_integer(items), 5)
        items = [-2, -4, 0]
        self.assertEqual(max_integer(items), 0)
        items = [2]
        self.assertEqual(max_integer(items), 2)
        items = []
        self.assertEqual(max_integer(items), None)
        items = [2, "string"]
        self.assertRaises(TypeError, max_integer(items))
