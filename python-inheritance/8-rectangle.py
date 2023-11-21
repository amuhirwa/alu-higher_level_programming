#!/usr/bin/python3
"""Module to design a rectangle"""


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


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initializes width and height of Rectangle
            Args:
                width(int): value of width of rectangle
                height(int): value of height of rectangle
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

print(issubclass(Rectangle, BaseGeometry))