#!/usr/bin/python3

def element_at(my_list, idx):

    # Use a loop with range to browse the index of list
    for idx in my_list range(0, 4):
        # If number to compare index is negatif, the list don't read
        if idx < 0:
            return None
        # If number to compare index is high , the list also don't read
        elif idx > 5:
            return None
        # Also print the number which find at the good index
        else:
            return my_list[idx]
