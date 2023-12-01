#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
