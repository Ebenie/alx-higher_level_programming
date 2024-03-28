#!/bin/bash
# This script fetches a URL's response body size using curl's silent mode
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

echo "$size"

