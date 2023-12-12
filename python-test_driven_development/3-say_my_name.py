#!/usr/bin/python3
"""Module to print name"""


def say_my_name(first_name, last_name=""):
    """Function to print name
        args:
            first_name(str)
            last_name(stsr)"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
