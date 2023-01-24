#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err))
        result = None

    return result
