#!/usr/bin/python3
"""Module to check if obj is an instance of specified class"""


def is_same_class(obj, a_class):
    """Function to check if obj is instance pf certain class"""
    if type(obj) == a_class:
        return True
    return False
