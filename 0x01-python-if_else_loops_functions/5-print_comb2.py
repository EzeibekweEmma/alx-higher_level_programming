#!/usr/bin/python3
# Program that prints numbers from 0 to 99
for number in range(0, 99):
    print("{:02d}, ".format(number), end="")

print("{:d}".format(99))