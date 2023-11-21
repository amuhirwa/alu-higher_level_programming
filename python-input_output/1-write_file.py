#!/usr/bin/python3
"""Module to read and print out a text file"""


def write_file(filename="", text=""):
    """Function to write to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
