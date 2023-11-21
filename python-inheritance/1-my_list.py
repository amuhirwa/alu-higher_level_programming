#!/usr/bin/python3
"""Prints list but sorted"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
