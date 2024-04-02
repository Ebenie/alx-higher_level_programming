#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and store the response in a temporary file
response_file=$(mktemp)
curl -s "$1" > "$response_file"

# Calculate the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size
echo "$response_size"

# Clean up the temporary file
rm "$response_file"

