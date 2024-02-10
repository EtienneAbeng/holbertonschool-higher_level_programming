#!/usr/bin/python3
'''
Le script devra retourne une static méthode qui retourne
le plus grand angle base sur l'aire
'''


class Rectangle:
    """Représente un rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ""  # Retourne une chaîne vide si le rectangle est vide

        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Retourne une représentation sous forme de chaîne de caractères du rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lors de la suppression d'une instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le rectangle avec la plus grande aire."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()
        
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
