#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0:
        return None

    elif idx > (len(my_list)):
        return new_list

    else:

        new_list =  my_list[:]
        new_list[3] = element

        return new_list
