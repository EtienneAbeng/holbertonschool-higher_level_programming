#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Vérifie si la liste est None
    if my_list is None:
        return None

    # Initialise un compteur pour suivre le nombre d'éléments imprimés
    elements_printed = 0

    # Utilise une boucle for pour parcourir la liste jusqu'à l'indice x
    for i in range(x):
        try:
            # Essaie d'imprimer l'élément à l'indice i
            print("{:d}".format(my_list[i]), end="")
            elements_printed += 1  # Incrémente le compteur
        except (ValueError, TypeError):
            # Gère les exceptions si l'élément n'est pas un entier
            break  # Sort de la boucle en cas d'erreur 

    # Ajoute un saut de ligne après l'impression des éléments
    print()
