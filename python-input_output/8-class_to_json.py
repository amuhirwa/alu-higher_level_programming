#!/usr/bin/python3
"""Module to return the dictionary description of a class"""


def class_to_json(obj):
    """Returns dictionary description of a class"""
    return obj.__dict__
