#!/usr/bin/python3
# Printing all numbers from 0 to 98 in decimal and in hexadecimal
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))
