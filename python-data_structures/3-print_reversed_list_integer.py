#!/usr/bin/python3

'''
Reverse interger - a function that prints all integers of a list,
in reverse order.
@my_list : the list of interger reversed
'''


def print_reversed_list_integer(my_list=[]):

    # Use a loop for with range to browse the index of the list
    # my_list -1 for
    for i in range(len(my_list) - 1, -1, -1):

        print("{:}".format(my_list[i]))
