#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    s = requests.Session()

    response = s.get(url)
    body = response.text

    status = response.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(body)
