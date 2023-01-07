#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_b:
        a1, a2 = tuple_a

        if len(tuple_b) < 2:
            b1, b2, b3= tuple_b + (0, 0)
        elif len(tuple_b) > 2:
               b1 = tuple_b[0]
               b2 = tuple_b[1]
        else:
            b1, b2 = tuple_b

        a = (a1 + b1, a2 + b2)
        return a
    else:
        return tuple_a
