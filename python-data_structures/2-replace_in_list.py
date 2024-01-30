#!/usr/bin/python3

'''
Replace element - write a function which repalce an element 
of a list a specific position

@idx: is negative, the function should not modify anything,
and returns the original list
@idx: is out of range (> of number of element in my_list), 
the function should not modify anything, and returns the original list
'''

def replace_in_list(my_list, idx, element):

    if idx < 0:
        return my_list

    elif idx > len(my_list):
        return my_list

    else:
        my_list[idx] = element
        return my_list


