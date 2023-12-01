#!/usr/bin/python3
"""Module to display body of response"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = parse.urlencode(data).encode()
    req = request.Request(url, data)
    with request.urlopen(req) as r:
        print(r.read().decode())
