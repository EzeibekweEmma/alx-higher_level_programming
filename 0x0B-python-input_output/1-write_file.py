#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    '''
    writing to a file and returning the number of characters written
    '''
    with open(filename, "w", encoding="UTF-8") as a:
        return a.write(text)
