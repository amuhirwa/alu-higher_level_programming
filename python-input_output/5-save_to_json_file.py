#!/usr/bin/python3
"""Module to save JSON representation to file"""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON to file
        Args:
            my_obj(object)
            filename
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
