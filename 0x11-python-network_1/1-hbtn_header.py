#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter 
and he value of the X-Request-Id variable
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)

