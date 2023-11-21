#!/usr/bin/python3
"""Module to design a rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initializes width and height of Rectangle
            Args:
                width(int): value of width of rectangle
                height(int): value of height of rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
