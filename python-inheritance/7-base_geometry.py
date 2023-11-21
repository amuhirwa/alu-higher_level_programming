#!/usr/bin/python3
"""Module to create a class called BaseGeometry"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Method to calculate raise exception for now"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate that value is a valid integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
