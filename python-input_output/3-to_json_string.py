#!/usr/bin/python3
"""Module for a function that returns json string of object"""
import json


def to_json_string(my_obj):
    """Converts object to JSON string
        Args:
            my_obj(object)
    """
    return json.dumps(my_obj)
