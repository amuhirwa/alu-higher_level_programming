#!/usr/bin/python3
"""Module to read and print out a text file"""


def write_file(filename="", text=""):
    """Function to write to a text file"""
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
        f.seek(0)
        return len(f.read())
