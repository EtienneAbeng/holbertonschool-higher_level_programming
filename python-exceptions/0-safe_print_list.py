def safe_print_list(my_list=[], x=0):
    try:
        count = 0  # Init un compteur pour suivre le nombre d'éléments imprimés
        for i in range(x):
            print(my_list[i], end="")  # imprimer l'élément à l'indice i
            count += 1  # Incrémente le compteur
        print()  # Ajoute un saut de ligne après l'impression des éléments
        return count  # Retourne le nombre d'éléments imprimés
    except IndexError:
        print()  # Ajoute un saut de ligne en cas d'erreur d'indice
        return count  #   imprime les nombres  même en cas d'erreur d'indice
