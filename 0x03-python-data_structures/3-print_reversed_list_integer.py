#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_len = len(my_list)

    if my_len > 0:
        for x in my_list:
            print("{:d}".format(my_list[my_len - x]))
