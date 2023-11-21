#!/usr/bin/python3
"""Module defines a square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
