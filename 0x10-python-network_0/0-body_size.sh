#!/bin/bash
# This script fetches a URL's response body size using curl's silent mode
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

