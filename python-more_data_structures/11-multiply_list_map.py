#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Utilise la fonction map avec une fonction créée avec def pour multiplier chaque élément
    def multiply(x):
        return x * number

    return list(map(multiply, my_list))

