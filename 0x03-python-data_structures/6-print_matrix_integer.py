#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for x in matrix:
            for y in x:
                print("{:d}".format(y), end=" ")
            print(end="\n")
    else:
        print()
