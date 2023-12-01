#!/usr/bin/python3
"""Module to display value of X-Request-Id in header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    print(r.headers["X-Request-Id"])
