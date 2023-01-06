#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for x in my_list:
        x -= 1
        print("{}".format(my_list[x]))
