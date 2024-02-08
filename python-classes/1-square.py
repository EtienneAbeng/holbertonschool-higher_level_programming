#!/usr/bin/python3
'''
Ce script définit une classe Square qui représente un carré.
La classe a un attribut privé __size qui représente la taille du côté du carré.
Lors de l'initialisation de la classe, la taille du carré est définie.
Si la taille n'est pas spécifiée, elle est définie par défaut à 0.

La classe a une vérification pour s'assurer que la taille est un entier positif
lors de l'initialisation.
Si la taille n'est pas un entier ou si négative, une exception est levée.
'''


class Square:
    '''Définit une classe Square.'''

    def __init__(self, size):
        '''Initialise un nouveau carré.

        Args:
            size (int): La taille du carré.
        '''
        self.__size = size  # Attribut privé pour stocker la taille du carré
