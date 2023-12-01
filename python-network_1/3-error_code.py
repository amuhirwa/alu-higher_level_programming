#!/usr/bin/python3
"""
Module to display body of response or error code
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as r:
            print(r.read().decode())
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
