#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
# Not allowed to use any pipe, redirection, etc.
# Not allowed to use ; and &&
# Uses curl
# Tested in sandbox provided, using the web server running on port 5000

curl -s -o /dev/null -w "%{http_code}" "$1"

