#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
import sys
sys.path.append("../")
import os
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test class for rectangle"""

    def test_instance(self):
        """Doc"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r4.id, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r11 = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r12 = Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r9 = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r13 = Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r14 = Rectangle(1, 2, 3, -4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(1, 2, 3, "4")

    def test_area(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.area(), 8)
