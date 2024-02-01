def square_matrix_simple(matrix=[]):
    # Création d'une nouvelle matrice avec les mêmes dimensions que l'origine
    new_matrix = []

    # Parcours des lignes de la matrice d'origine
    for row in matrix:
        new_row = []  # Nouvelle ligne pour la new matrice
        # Parcours des éléments de chaque ligne
        for element in row:
            new_row.append(element**2)  # Ajout du carré à la nouvelle ligne
        new_matrix.append(new_row)  # Ajout nouvelle ligne à la new matrice

    return new_matrix
