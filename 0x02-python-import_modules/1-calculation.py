#!/usr/bin/python3
# program that imports maths functions from the file calculator_1

if __name__ == "__main__":
    """
    program that imports maths functions from the file calculator_1
    """
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
