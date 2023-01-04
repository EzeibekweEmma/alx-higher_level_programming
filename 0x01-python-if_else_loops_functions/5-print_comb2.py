#!/usr/bin/python3
# Program that prints numbers from 0 to 99
for i in range(100):
    if i != 99:
        print("{}".format('0' + str(i) if i < 10 else i), end=", ")
    else:
        print(i)
