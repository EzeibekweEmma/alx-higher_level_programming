#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        num = my_list[0]
        for x in my_list:
            if num <= x:
                num = x
            else:
                continue

        return num
    else:
        return None
