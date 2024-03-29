#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter 
and he value of the X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)

