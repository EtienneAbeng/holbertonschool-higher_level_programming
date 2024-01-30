#!/usr/bin/python3

'''
Reverse interger - a function that prints all integers of a list,
in reverse order.
@my_list : the list of interger reversed
'''


def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
