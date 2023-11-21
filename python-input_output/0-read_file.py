#!/usr/bin/python3
"""Module to read and print out a text file"""


def read_file(filename=""):
    """Function to print content of a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
