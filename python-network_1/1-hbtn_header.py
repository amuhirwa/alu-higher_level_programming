#!/usr/bin/python3
"""Module to display value of X-Request-Id in header"""
import urllib.request
import sys

r = urllib.request.urlopen(sys.argv[1])
print(r.headers["X-Request-Id"])
