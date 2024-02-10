def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur donné.

    Args:
        matrix (list de listes): La matrice à diviser.
        div (int ou float): Le diviseur.

    Returns:
        list de listes: Une nouvelle matrice avec les éléments divisés par le diviseur.

    Raises:
        TypeError: Si la matrice n'est pas une liste de listes d'entiers/flottants
                   ou si div n'est pas un nombre.
        ZeroDivisionError: Si div est égal à 0.

    """
    # Vérifie si la matrice est une liste de listes d'entiers/flottants
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix doit être une matrice (liste de listes) d'entiers/flottants")

    # Vérifie si tous les éléments de la matrice sont des entiers/flottants
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix doit être une matrice (liste de listes) d'entiers/flottants")

    # Vérifie si chaque ligne de la matrice a la même taille
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Chaque ligne de la matrice doit avoir la même taille")

    # Vérifie si div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div doit être un nombre")

    # Vérifie si div est différent de zéro
    if div == 0:
        raise ZeroDivisionError("division par zéro")

    # Divise chaque élément de la matrice par div et arrondit à 2 décimales
    return [[round(num / div, 2) for num in row] for row in matrix]

# Exemple d'utilisation :
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
