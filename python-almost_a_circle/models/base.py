#!/usr/bin/python3
"""
Module base pour la gestion des identifiants uniques des instances.
"""

import json

class Base:
    """
    Classe de base pour gérer les identifiants uniques des instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructeur de la classe Base.

        Args:
            id (int, optionnel): Identifiant de l'instance. Si non spécifié,
                un identifiant unique sera généré automatiquement.
        """

        if id is not None:  # si id est donné
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # incrémentation et assignation

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convertit une liste de dictionnaires en chaîne JSON.

        Args:
            list_dictionaries (list): Liste de dictionnaires à convertir.

        Returns:
            str: Chaîne JSON représentant la liste de dictionnaires.
        """
        if list_dictionaries is None:
            return "[]"  # Retourne une chaîne JSON vide si la liste de dictionnaires est None
        elif len(list_dictionaries) == 0:
            return "[]"  # Retourne une chaîne JSON vide si la liste de dictionnaires est vide
        else:
            return json.dumps(list_dictionaries)  # Convertit la liste de dictionnaires en chaîne JSON

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Écrit la représentation JSON en chaîne de list_objs dans un fichier.

        Args:
            list_objs (list): Liste d'instances héritant de la classe Base.
        """
        filename = cls.__name__ + ".json"  # Nom du fichier basé sur le nom de la classe
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")  # Écrit une liste JSON vide si list_objs est None
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]  # Convertit les objets en dictionnaires
                json_str = cls.to_json_string(dict_list)  # Convertit la liste de dictionnaires en chaîne JSON
                file.write(json_str)  # Écrit la chaîne JSON dans le fichier

    @staticmethod
    def from_json_string(json_string):
        """
        Convertit une chaîne JSON en liste de dictionnaires.

        Args:
            json_string (str): Chaîne JSON à convertir.

        Returns:
            list: Liste de dictionnaires.
        """
        if json_string is None or json_string == "":
            return []  # Return liste vide si la chaîne JSON est None ou vide
        else:
            return json.loads(json_string)  # Convertit la chaîne JSON en liste de dictionnaires

    @classmethod
    def create(cls, **dictionary):
        """
        Crée une instance avec tous les attributs déjà définis.

        Args:
            dictionary (dict): Dictionnaire contenant les attributs de l'instance.

        Returns:
            Base: Instance avec les attributs définis.
        """
        if cls.__name__ == "Rectangle":
            # Si la classe est Rectangle
            dummy_instance = cls(1, 1)  # Crée une instance "dummy" avec des valeurs arbitraires
        elif cls.__name__ == "Square":
            # Si la classe est Square
            dummy_instance = cls(1)  # Crée une instance "dummy" avec des valeurs arbitraires
        else:
            return None

        dummy_instance.update(**dictionary)  # Applique les vraies valeurs à l'instance "dummy"
        return dummy_instance

