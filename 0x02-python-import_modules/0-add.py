#!/usr/bin/python3

if __name__ == "__main__":
    """Program that imports function def add(a, b), from the file add_0.py"""
    import add_0

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add_0.add(a, b)))
