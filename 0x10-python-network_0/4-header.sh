#!/bin/bash
# This script sends a GET request to a URL and displays the response body, including X-School-User-Id header with value 98
curl -s -H "X-School-User-Id: 98" "$1"

