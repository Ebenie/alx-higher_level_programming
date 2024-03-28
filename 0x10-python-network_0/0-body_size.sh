#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and store response body
response_body=$(curl -s -o /dev/null -w "%{size_download}\n" "$1")

# Display the size of the response body in bytes
echo "$response_body"

