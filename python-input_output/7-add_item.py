#!/usr/bin/python3
"""Module that adds all arguments to a Python list, and then saves them to a file"""
from sys import argv as arg
to_json = __import__("5-save_to_json_file.py").save_to_json_file
from_json = __import__("6-load_from_json_file.py").load_from_json_file

filename = "add_item.json"
with open(filename, "a+") as f:
    if len(f.read()) == 0:
        arr = []
        to_json(arr, f)
    else:
        arr = from_json(f)
        for i in arg:
            arr.append(i)
        to_json(arr, f)
