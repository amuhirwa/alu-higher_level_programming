#!/usr/bin/python3
"""Module to log into github"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    result = r.json()
    print(result.id)
