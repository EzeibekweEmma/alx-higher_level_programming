#!/usr/bin/python3
# Program that imports the function def add(a, b), from the file add_0.py
import add_0

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))
