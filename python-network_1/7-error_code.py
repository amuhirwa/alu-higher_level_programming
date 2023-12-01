#!/usr/bin/python3
"""Module to print error code"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    
    if r.code >= 400:
        print("Error code:", r.code)
    else:
        print(r.text)
