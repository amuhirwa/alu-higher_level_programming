#!/usr/bin/python3
"""Module to create a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """Getters and setters for width and height"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
            Attrs:
                value: value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
            Attrs:
                value: value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
