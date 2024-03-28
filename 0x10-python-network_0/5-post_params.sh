#!/bin/bash
# This script sends a POST request to a URL and displays the response body, including email and subject variables
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

