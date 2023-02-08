#!/usr/bin/python3
"""
JSON Module imported
"""
import json


def load_from_json_file(filename):
    '''
    creating an Object from a JSON file
    '''
    with open(filename) as a:
        obj_file = a.read()
        return json.loads(obj_file)
