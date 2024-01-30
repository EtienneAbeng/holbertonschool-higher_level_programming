#!/usr/bin/python3

def element_at(my_list, idx):

        # If number to compare index is negatif, the list don't read
        if idx < 0:
            return None

        elif idx > len(my_list):
            return None
        # Also print the number which find at the good index
        else:
            return my_list[idx]
