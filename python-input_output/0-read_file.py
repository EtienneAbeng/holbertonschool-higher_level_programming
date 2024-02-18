#!/usr/bin/python3
"""
Le script est une fonction qui lit a fichier-text(UTF8)
et affiche le contenu en sortie standard
"""


def read_file(filename=""):
    """Lire le contenu du fichier et l'afficher sur la stdout
    Args:
        filename: Le chemin vers le fichier à lire
    """
    # Ouverture du fichier en mode read avec encode utf-8
    with open(filename, "r", encoding="utf-8") as f:
        # Lit le contenu se trouvant dans le fichier
        text = f.read()
        print(text, end="")  # Affiche le contenu du fichier
