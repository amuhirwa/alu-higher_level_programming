#!/usr/bin/python3
"""
Module displays body of response
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except error.HTTPError as e:
        print(f"Error code:", e.code)
