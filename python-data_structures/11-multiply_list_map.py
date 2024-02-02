def multiply_list_map(my_list=[], number=0):
    # Utilise la fonction map pour multiplier chaque élément de la liste par le nombre donné
    # Convertit ensuite le résultat en liste
    return list(map(lambda x: x * number, my_list))
