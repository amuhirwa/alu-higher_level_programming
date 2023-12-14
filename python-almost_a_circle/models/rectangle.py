#!/usr/bin/python3
"""Module defines rectangle class"""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates Rectangle"""
        Base().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
