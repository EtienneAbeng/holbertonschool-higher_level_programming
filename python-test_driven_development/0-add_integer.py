#!/usr/bin/python3
""" Programme de calcul de somme d'entiers """

def add_integer(a, b=98):
    """ Ajoute deux entiers ou flottants.

    Args:
        a (int ou float): Le premier nombre. Par défaut, 98.
        b (int ou float): Le deuxième nombre. Par défaut, 98.

    Raises:
        TypeError: Si a ou b n'est pas un entier ou un flottant.

    Returns:
        int: La somme des deux nombres convertie en entier.
    """

    # Message d'erreur commun
    message_erreur = " doit être un entier"

    # Vérifie si a est un entier ou un flottant
    if type(a) not in [int, float]:
        raise TypeError("a" + message_erreur)
    
    # Vérifie si b est un entier ou un flottant
    if type(b) not in [int, float]:
        raise TypeError("b" + message_erreur)

    # Convertit a et b en entiers puis retourne leur somme
    va, vb = int(a), int(b)
    return va + vb

