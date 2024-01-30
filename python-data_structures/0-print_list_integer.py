#!/usr/bin/python3
'''
list of integer - Write a function that prints all integers of a list.
@str.format : use this format to print the list
@len : len(ma_liste) pour déterminer la condition de fin de la boucle
'''


def print_list_integer(my_list=[]):

    # Initialize the counter index to browse the list
    i = 0
    # Browse the list with i to print the list
    while i < len(my_list):
        print("{:d}".format(my_list[i]))
        # Each end of iteration to add + 1 at the counter
        i += 1
