#!/usr/bin/python3
"""Module to add 2 integers"""

def add_integer(a, b=98):
    """Function to add 2 numbers
        Args:
            a(int)
            b(int)"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
