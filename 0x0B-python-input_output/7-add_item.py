#!/usr/bin/python3
'''
sys module imported
save_to_json_file imported
load_from_json_file imported
'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file('add_item.json')
except FileNotFoundError:
    data = []

add_data = data + sys.argv[1:]
save_to_json_file(add_data, 'add_item.json')
