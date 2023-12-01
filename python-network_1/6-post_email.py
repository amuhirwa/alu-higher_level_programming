#!/usr/bin/python3
"""Module to post email"""
import sys
import requests

url = sys.argv[1]
email = {'email': sys.argv[2]}

r = requests.post(url, email)
print(r.text)
