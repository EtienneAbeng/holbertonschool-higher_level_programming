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

    number_of_instances = 0  # attribut classe pour suivre le nombre instance
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        '''
        initialise un rectangle avec une largeur et une hauteur
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1 # incremente à chaque instantation

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

    @property
    def width(self):
        """Getter pour récupérer la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour définir la largeur du rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour récupérer la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour définir la hauteur du rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation sous forme de chaîne de caractères du rectangle."""
        if self.width == 0 or self.height == 0:
            return ""  # Retourne une chaîne vide si le rectangle est vide

        for i in range(self.height):  # Boucle sur les lignes du rectangle
            for j in range(self.width):  # Boucle sur les colonnes du rectangle
                print(self.print_symbol, end='')  # Imprime le caractère '#' sans sauter de ligne
            if i != self.height - 1:  # Si ce n'est pas la dernière ligne
                print()  # Passe à la ligne suivante
        return ''  # Retourne une chaîne vide après l'impression du rectangle

    def __repr__(self):
        """Retourne une representation sous forme de chaine de caractere"""
        return f"rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Retourne une representation sous forme de chaine de caractere"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Décremente 1 à 1 à chaque suppres
