#!/usr/bin/python3
"""Prints list but sorted"""


class MyList(list):
    """Class MyList inherits list."""

    def print_sorted(self):
        """Prints sorted lists."""
        print(sorted(self))
