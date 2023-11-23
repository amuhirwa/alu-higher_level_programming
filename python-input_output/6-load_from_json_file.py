#!/usr/bin/python3
"""Module to load from JSON file"""
import json


def load_from_json_file(filename):
    """Function to load from JSON file
        Args:
              filename(str): name of JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
