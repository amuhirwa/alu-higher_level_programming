#!/usr/bin/python3
"""Module to define a square class"""


class Square:
    """Class to define a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method to calculate area of Square"""
        return self.__size * self.__size

    @property
    """Getters and setters for the size attribute"""
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
