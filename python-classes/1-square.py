#!/usr/bin/python3
'''Écrivez une classe Square qui définit un carré

Attribut d'instance privée : taille
Instanciation avec taille (pas de vérification de type/valeur)
'''

class Square:
    """Définit une classe Square."""

    def __init__(self, size):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du carré.
        """
        self.__size = size  # Attribut privé pour stocker la taille du carré

