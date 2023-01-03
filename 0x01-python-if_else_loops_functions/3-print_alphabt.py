#!/usr/bin/python3
# Printing alphabet in lowercase using the ASCII except q and e
for letter in range(97, 123):
    if 101 != letter != 113:
        print("{:c}".format(letter), end="")
