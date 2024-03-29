#!/usr/bin/python3

'''
Ce script définit une classe Square qui représente un carré. 
La classe a un attribut privé __size qui représente la taille du côté du carré. 
Lors de l'initialisation de la classe, la taille du carré est définie. 
Si la taille n'est pas spécifiée, elle est définie par défaut à 0.

La classe a une vérification pour s'assurer que la taille est un entier positif 
lors de l'initialisation. 
Si la taille n'est pas un entier ou si elle est négative, une exception est levée.
'''

# Définition de la classe Square
class Square:
    '''Définit une classe Square pour représenter un carré.'''

    # Méthode d'initialisation pour créer un nouvel objet Square
    def __init__(self, size=0):
        '''Initialise un nouveau carré avec une taille donnée.

        Args:
            size (int, optional): La taille du côté du carré (par défaut 0).
        '''
        # Vérifie si la taille est un entier et si elle > ou ==  0
        if not isinstance(size, int):
            raise TypeError("size must be an integer") # Lève une exception
        if size < 0:
            raise ValueError("size must be >= 0")  # Lève une exception

        self.__size = size
