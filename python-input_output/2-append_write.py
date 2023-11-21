#!/usr/bin/python3
"""Module to append and print out a text file"""


def append_write(filename="", text=""):
    """Function to append to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
