#!/usr/bin/python3
"""
Defines a text file-reading function
"""

def read_file(filename=""):
    """
    reading a file
    """
    with open(filename, encoding="UTF-8") as a:
        print(a.read(), end="")
