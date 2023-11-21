#!/usr/bin/python3
"""Module to check if an instance inherits from a specified class"""


def inherits_from(obj, a_class):
    """Function to check if instance inherits from certain class"""
    if type(obj).__base__ == a_class:
        return True
    return False
