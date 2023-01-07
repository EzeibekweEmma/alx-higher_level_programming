#!/usr/bin/python3
# function that prints a string in uppercase


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[i]) - letter), end='')
    print()
