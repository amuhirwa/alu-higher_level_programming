#!/usr/bin/python3
"""Prints list but sorted"""


class MyList(list):
    """Subclass of list"""
    def print_sorted(self):
        print(sorted(self))
