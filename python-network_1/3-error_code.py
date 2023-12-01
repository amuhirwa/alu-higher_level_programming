#!/usr/bin/python3
"""
Module displays body of response
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys
    
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
