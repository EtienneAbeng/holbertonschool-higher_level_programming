#!/usr/bin/python3

'''
Le script definit une classe rectangle pour representer ce rectangle
La class a 2 attributs privée __height et __weight du rectangle
Les méthodes de propriété pour récupérer sont getter et setter
'''


class Rectangle:
    '''
    definit une classe rectangle pour representer le rectangle
    '''

    def __init__(self, width=0, height=0):
        '''
        initialise un rectangle avec une largeur et une hauteur
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter pour recuperer la largeur du rectangle
        '''
        return self.__width  # retourne la largeur du rectangle

    @width.setter
    def width(self, value):
        '''
        Setter pour définir la hauteur du rectangle

        Agrs:
            value(int): la nouvelle valueur de la largeur

        Raise:
            TypeError: si la largeur n'est pas un entier
            ValueError: si la largeur est négative
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # verifie si un entier
        elif value < 0:
            raise ValueError("width must >= 0")  # verifie largeur est positive
        else:
            self.__width = value

        @property
        def height(self):
            '''
            Getter pour recupérer la hauteur
            '''
            return self.__height  # la hauteur du rectangle

        @height.setter
        def height(self, height):
            '''
            Setter pour définir la hauteur du rectangle

            Args:
                value(int): la nouvelle valeur de la hauteur

            Raise:
                TypeError: vérifie la hauteur n'est un type entier
                ValueError: vérifie si la hauteur n'est pas un entier négative
            '''
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must >= 0")
            else:
                self.__height = value
