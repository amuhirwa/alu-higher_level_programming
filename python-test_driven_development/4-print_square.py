#!/usr/bin/python3
"""Module to print square"""


def print_square(size):
    """Function to print square of #
        args:
            size(int): size of square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#"*size) for i in range(size)]
