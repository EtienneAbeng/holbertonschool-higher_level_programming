class BaseGeometry:
    """
    Une base class qui représente une géométrie.
    """

    def area(self):
        """
        Calcule l'aire de la géométrie
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide si la valeur passée est bien un entier positif

        Args:
            name (str): Le nom de la valeur à valider.
            value (int): La valeur à valider.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur n'est pas un entier positif.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be a positive integer".format(name))


class Rectangle(BaseGeometry):
    """
    La classe Rectangle représente un rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur spécifiées.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Retourne une chaîne de caractères du rectangle.

        Returns:
            str: Une représentation d'une chaîne de caractères du rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calcule et retourne la valeur de l'aire du rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    La classe Square représente un carré, héritant de la classe Rectangle.
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille spécifiée.

        Args:
            size (int): La taille du carré.
        """
        super().__init__(size, size)  # Appel méthode __init__() classe parente
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """
        Retourne une représentation d'une chaîne de caractères du carré.

        Returns:
            str: Une représentation d'une chaîne de caractères du carré.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
