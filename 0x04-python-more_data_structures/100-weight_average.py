#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        w = 0
        s = 0
        for x in my_list:
            w += x[1]
            s += (x[0] * x[1])

        av = s / w
        return av
    else:
        return 0
