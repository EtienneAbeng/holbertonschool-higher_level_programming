#!/usr/bin/python3

'''
Un script avec une classe Mylist qui hérite d'une liste et affiche la liste
mais trier dans croissant en tri ascendant
'''


class MyList(list):
    """Une sous-classe de list avec une méthode supplémentaire"""

    def append(self, element):
        """Ajoute un élément à la liste s'il s'agit d'un entier"""

        if not isinstance(element, int):
            raise TypeError("The value must an integer")
        super().append(element)

    def print_sorted(self):
        """Imprime la liste triée"""

        sorted_list = sorted(self)
        print(sorted_list)
