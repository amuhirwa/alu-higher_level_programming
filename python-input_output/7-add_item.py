#!/usr/bin/python3
"""Module that adds all arguments to a Python list,
and then saves them to a file"""

from sys import argv as arg
to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
with open(filename, "a+") as f:
    try:
        arr = from_json(filename)
    except:
        arr = []
    for i in arg[1:]:
        arr.append(i)
    to_json(arr, filename)
