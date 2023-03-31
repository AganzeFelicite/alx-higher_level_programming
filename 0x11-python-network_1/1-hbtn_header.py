#!/usr/bin/python3
"""
this is a script that takes in a response to a
url and print the value of a key in the header
response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    url_req = urllib.request.Request(url)
    with urllib.request.urlopen(url_req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
