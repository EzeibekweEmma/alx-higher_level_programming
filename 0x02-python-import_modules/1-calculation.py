#!/usr/bin/python3
# program that imports maths functions from the file calculator_1

if __name__ == "__main__":
    """
    program that imports maths functions from the file calculator_1
    """
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))