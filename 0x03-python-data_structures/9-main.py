#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
my_list2 = [-7, -6, -12, -3, -34, -10, -4]
my_list3 = []
max_value = max_integer(my_list)
max_value2 = max_integer(my_list2)
max_value3 = max_integer(my_list3)
print("Max: {}".format(max_value))
print("Max: {}".format(max_value2))
print("Max: {}".format(max_value3))
