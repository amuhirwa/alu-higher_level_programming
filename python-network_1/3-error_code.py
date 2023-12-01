#!/usr/bin/python3
"""
Module to display body of response or error code
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    url = sys.argv[1]
    try:
        with request.urlopen(url) as r:
            print(r.read().decode())
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
