#!/usr/bin/python3
"""Module to read and print out a text file"""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
