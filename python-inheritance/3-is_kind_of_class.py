#!/usr/bin/python3
"""Module to check if an instance of specified class or inherits from it"""


def is_kind_of_class(obj, a_class):
    """Function to check if instance inherits from certain class
     or is of that class"""
    if type(obj) == a_class:
        return True
    if issubclass(type(obj), a_class):
        return True
    return False
