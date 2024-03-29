#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response.
It handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)

