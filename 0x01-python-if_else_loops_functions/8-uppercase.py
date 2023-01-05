#!/usr/bin/python3
# function that prints a string in uppercase
def uppercase(str):
    for i in str:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            i = chr((ord(i) - ord('a')) + ord('A'))
        print("{}".format(i), end="")
    print()
