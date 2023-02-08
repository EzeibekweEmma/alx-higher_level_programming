#!/usr/bin/python3

def read_file(filename=""):
    """
    reading a file
    """
    with open(filename,  encoding="UTF-8") as a:
        print(a.read())
