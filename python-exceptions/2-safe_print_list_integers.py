#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        # Initialise un compteur pour le nombre d'entiers imprimés
        count = 0
        # Boucle à travers les éléments de my_list jusqu'à x
        for i in range(x):
            # Vérifie si l'élément est un entier
            if isinstance(my_list[i], int):
                # Utilise "{:d}".format() pour imprimer l'entier
                print("{:d}".format(my_list[i]), end="")
                # Incrémente le compteur
                count += 1
        # Imprime une nouvelle ligne
        print()
        # Retourne le nombre d'entiers imprimés
        return count
    except (ValueError, TypeError, IndexError):
        # En cas d'erreur (ValueError, TypeError ou IndexError)
        return 0
