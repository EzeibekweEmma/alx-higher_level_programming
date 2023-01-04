#!/usr/bin/python3
# function that prints the numbers from 1 to 100 separated by a space.
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            msg = "FizzBuzz"
        elif n % 3 == 0:
            msg = "Fizz"
        elif n % 5 == 0:
            msg = "Buzz"
        else:
            msg = str(n)

        print("{:s}".format(msg), end=' ')
