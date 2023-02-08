#!/usr/bin/python3
'''
JSON Module imported
'''
import json


def from_json_string(my_str):
    '''
    Returns an object from a json
    '''
    return json.loads(my_str)
