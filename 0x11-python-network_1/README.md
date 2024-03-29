

README



This directory contains a collection of Python scripts for various network-related tasks. Each script is designed to perform a specific function and utilizes different Python packages such as urllib, requests, and built-in libraries like sys. Below is a brief description of each script along with usage instructions.

1. 0-hbtn_status.py
This script fetches the status of https://alx-intranet.hbtn.io/status using the urllib package. It demonstrates how to make a GET request and retrieve the response using urllib.

2. 1-hbtn_header.py
This script sends a POST request to a specified URL with an email parameter using the urllib package. It also extracts and prints the value of the X-Request-Id variable from the response header.

3. 2-post_email.py
Similar to the previous script, this one sends a POST request with an email parameter using urllib. However, it also decodes the body of the response in UTF-8 format before printing it.

4. 3-error_code.py
This script sends a GET request to a specified URL using urllib. It handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.

5. 4-hbtn_status.py
This script fetches the status of https://alx-intranet.hbtn.io/status using the requests package. It demonstrates how to make a GET request and retrieve the response using requests.

6. 5-hbtn_header.py
Similar to script 2, this one sends a GET request to a specified URL using the requests package. It extracts and prints the value of the X-Request-Id variable from the response header.

7. 6-post_email.py
This script sends a POST request to a specified URL with an email parameter using the requests package. It then displays the body of the response.

8. 7-error_code.py
This script sends a GET request to a specified URL using the requests package. It also handles HTTP errors and prints the HTTP status code in case of an error.

9. 8-json_api.py
This script sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter using the requests package. It then displays the response data in a specific format.

10. 10-my_github.py
This script uses the GitHub API to display the user id. It utilizes Basic Authentication with a personal access token as the password to access user information.
