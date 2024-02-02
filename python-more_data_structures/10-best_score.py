def best_score(a_dictionary):
    # Vérifie si le dictionnaire est None
    if a_dictionary is None:
        return None

    # Initialise les variables pour stocker la best_key et best_value
    best_key = None
    best_value = None  # Initialise à une valeur négative infinie

    # Parcourt chaque paire clé-valeur dans le dictionnaire
    for key, value in a_dictionary.items():
        # Compare la valeur actuelle avec la meilleure valeur trouvée jusqu'à présent
        if value > best_value:
            # Met à jour la meilleure clé et la meilleure valeur
            best_key = key
            best_value = value

    # Retourne la meilleure clé
    return best_key
