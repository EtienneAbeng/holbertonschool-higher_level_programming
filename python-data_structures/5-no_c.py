#!/usr/bin/python5

'''
Remove character -  a function that removes all characters c and C from a string
@my_string: contain the old string character
@new_String: cointain the new string character after removing
'''


def no_c(my_string):


    # Initialyze a new string a character null
    new_String = ""
    # Use a loop with range with len to browse the string
    for idx in range(0, len(my_string)):
        # If the string is different of 'c' or 'C' also print
        if my_string[idx] != 'c' and my_string[idx] != 'C':
           # Assign the new string character without 'c' or 'C'
           # += is used to concatenat new_String + my_string
           new_String += my_string[idx]
   # Return the new string
    return new_String
