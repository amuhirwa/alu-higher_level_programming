#!/usr/bin/python3
"""Module to display value of X-Request-Id in header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers["X-Request-Id"])
