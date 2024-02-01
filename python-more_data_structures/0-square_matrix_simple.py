def square_matrix_simple(matrix=[]):
    # Création d'une nouvelle matrice avec les mêmes dimensions que la matrice d'origine
    new_matrix = []
    
    # Parcours des lignes de la matrice d'origine
    for row in matrix:
        new_row = []  # Nouvelle ligne pour la nouvelle matrice
        # Parcours des éléments de chaque ligne
        for element in row:
            new_row.append(element**2)  # Ajout du carré de l'élément à la nouvelle ligne
        new_matrix.append(new_row)  # Ajout de la nouvelle ligne à la nouvelle matrice
    
    return new_matrix
