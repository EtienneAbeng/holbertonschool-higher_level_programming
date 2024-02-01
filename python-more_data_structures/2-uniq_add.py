#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Vérifier si la liste est None, dans ce cas, retourner 0
    if my_list is None:
        return 0

    # Convertir la liste en ensemble pour obtenir les nombres uniques
    unique_numbers = set(my_list)

    # Calculer la somme des nombres uniques en utilisant la fonction sum
    result = sum(unique_numbers)

    # Retourner la somme des nombres uniques
    return result
