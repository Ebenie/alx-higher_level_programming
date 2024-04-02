#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
# Sends a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
# Uses curl
# Tested in sandbox provided, using the web server running on port 5000

json_file="$2"
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$1")
if [[ $response == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi

