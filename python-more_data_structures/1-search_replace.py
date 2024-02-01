#!/usr/bin/python3

def search_replace(my_list, search, replace):

    if my_list is None:
        return None

    new_list = my_list.copy()

    for idx in range(len(new_list)):
        if search  == new_list[idx]: 
            new_list[idx] = replace

    return (new_list)
