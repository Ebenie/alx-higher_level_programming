#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
# Uses curl
# Not allowed to use echo, cat, etc. to display the final result
# Tested in sandbox provided, using the web server running on port 5000

curl -s -L -X PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me

