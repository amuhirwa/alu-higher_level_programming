#!/usr/bin/python3
"""Module to create a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Function to calculate area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function to calculate perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        print_symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height - 1):
            rect += (print_symbol * self.__width) + "\n"
        rect += print_symbol * self.__width
        return rect

    def __repr__(self):
        return f'Rectangle{self.__width, self.__height}'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
