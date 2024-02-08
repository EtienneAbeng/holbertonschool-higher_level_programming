#!/usr/bin/python3

'''
Ce script définit une classe Square qui représente un carré.
La classe a un attribut privé __size qui représente la taille du côté du carré.
Lors de l'initialisation de la classe, la taille du carré est définie.
Si la taille n'est pas spécifiée, elle est définie par défaut à 0.

La classe a une vérification pour s'assurer que la taille est un entier positif
lors de l'initialisation.
Si la taille n'est pas un entier ou
si elle est négative, une exception est levée.

La classe a également une méthode area qui calcule et retourne l'aire du carré,
ainsi qu'une méthode my_print qui affiche le carré avec des #.
'''


class Square:
    '''Définit une classe Square pour représenter un carré.'''

    def __init__(self, size=0):
        '''Initialise un carré avec une taille donnée (par défaut 0).'''
        self.size = size  # Définit la taille du carré

    @property
    def size(self):
        '''Getter pour récupérer la taille du carré'''
        return self.__size  # Retourne la taille du carré

    @size.setter
    def size(self, value):
        '''Setter pour définir la taille du carré.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Définit la taille du carré

    def area(self):
        '''alcule et retourne l'aire du carré'''
        return self.__size ** 2  # Calcule l'aire du carré

    def my_print(self):
        '''Affiche le carré avec des #'''
        if self.__size == 0:
            print()  # Affiche une ligne vide si la taille est 0
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  # Affiche une ligne de #
