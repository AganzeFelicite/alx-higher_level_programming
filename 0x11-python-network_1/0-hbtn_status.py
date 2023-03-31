#!/usr/bin/python3
"""
this is a python script that
fetch content of the 
the url provide in the code
and displays it in the format
shown
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response: $")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf-8 content: {}".format(data.decode("utf-8")))
