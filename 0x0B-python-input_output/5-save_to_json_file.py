#!/usr/bin/python3
'''
JSON Module imported
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an Object to a text file,
    using a JSON representation
    '''
    with open(filename, 'w') as a:
        data = json.dumps(my_obj)
        a.write(data)
