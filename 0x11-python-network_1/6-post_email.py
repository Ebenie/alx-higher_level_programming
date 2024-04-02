#!/usr/bin/python3
"""Python script that sends a POST request to a specified URL with an email address"""
import requests
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter,
    and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to be sent.

    Returns:
        None
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed to send POST request.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 6-post_email.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    post_email(url, email)

