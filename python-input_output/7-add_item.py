#!/usr/bin/python3
"""
Ajoute tous les arguments à une liste Python, 
puis les sauvegarde dans un fichier.
"""

import sys
import json
from os import path

# Importe la fonction pour sauvegarder une liste au format JSON
from save_to_json_file import save_to_json_file

# Importe la fonction pour charger une liste depuis un fichier JSON
from load_from_json_file import load_from_json_file

# Nom du fichier de sauvegarde
filename = "add_item.json"

# Initialise une liste vide pour stocker les arguments
args_list = []

# Vérifie si le fichier existe déjà
if path.exists(filename):
    # Charge le contenu du fichier dans la liste
    args_list = load_from_json_file(filename)

# Ajoute les arguments fournis en ligne de commande à la liste
args_list.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(args_list, filename)
