#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""

    s = requests.Session()

    data = {'q': letter}
    response = s.post(url, data=data)
    try:
        body = response.json()
        if body == {}:
            msg = 'No result'
        else:
            msg = '[{}] {}'.format(body['id'], body['name'])
    except ValueError:
        msg = 'Not a valid JSON'

    print(msg)
