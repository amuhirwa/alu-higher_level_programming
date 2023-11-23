#!/usr/bin/python3
"""Module to return object from JSON"""
import json


def from_json_string(my_str):
    """Function to return object from JSON
        Args:
            my_str(str): JSON string
    """
    return json.loads(my_str)
