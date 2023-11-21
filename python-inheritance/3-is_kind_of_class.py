#!/usr/bin/python3
"""Module to check if an instance of specified class or inherits from it"""


def is_kind_of_class(obj, a_class):
    if type(obj) == a_class:
        return True
    if type(obj).__base__ == a_class:
        return True
    return False
