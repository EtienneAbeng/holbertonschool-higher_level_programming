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

        Args:
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
    def height(self, value):
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

    def area(self):
        '''
        Calcule et return l'aire du rectangle en multipliant width * height
        '''
        return self.__width * self.__height  # retrourne l'air du carré

    def perimeter(self):
        '''
        Calcule et retourne le périmètre du rectangle en addtionnant
        height + width et ensuite multipliant l'ensemble par 2
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2  # return le périmetre

    def __str__(self):
        """Retourne une représentation sous forme de chaîne de caractères du rectangle."""
        if self.width == 0 or self.height == 0:
            return ""  # Retourne une chaîne vide si le rectangle est vide

        result = ''
        for i in range(self.height):  # Boucle sur les lignes du rectangle
            for j in range(self.width):  # Boucle sur les colonnes du rectangle
                result += '#'  # Ajoute le caractère '#' à la chaîne résultante
            if i != self.height - 1:  # Si ce n'est pas la dernière ligne
                result += '\n'  # Ajoute un saut de ligne à la chaîne résultante
        return result  # Retourne la chaîne résultante

    def __repr__(self):
        """Retourne une representation sous forme de chaine de caractere"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Retourne une representation sous forme de chaine de caractere"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Décremente 1 à 1 à chaque suppres
