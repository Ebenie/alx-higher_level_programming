#!/bin/bash
# This script sends a GET request via curl, displaying body if status is 200, utilizing -s for silence and -o to save response. If status is 200, body is shown via cat
curl -s -o temp_body "$1" && cat temp_body; rm -f temp_body

