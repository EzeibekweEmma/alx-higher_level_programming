#!/usr/bin/python3
# program that prints the ASCII alphabet, in reverse order, alternating
#        lowercase and uppercase
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(letter if letter % 2 == 0 else letter - 32), end='')
