#!/bin/bash

# Check if curl is available
if ! command -v curl &> /dev/null; then
  echo "Error: curl is not installed. Please install curl before running this script."
  exit 1
fi

# Get the URL from the first argument
url="$1"

# Check if a URL is provided
if [[ -z "$url" ]]; then
  echo "Error: Please provide a URL as an argument."
  echo "Usage: $0 <url>"
  exit 1
fi

# Use curl to get the response header size only (option -s silent, -I header only)
response_size=$(curl -sI "$url" 2>/dev/null | grep -i Content-Length | awk '{print $2}')

# Check if size was found
if [[ -z "$response_size" ]]; then
  echo "Error: Could not determine response size for URL: $url"
  exit 1
fi

# Display size in bytes
echo "Response size for $url: $response_size bytes"

