#!/bin/bash

-- <CREATE TABLE IF NOT EXISTS> Crée une table nommée id_not_null si elle n'existe pas déjà
-- <id INT DEFAULT 1> Définit une colonne id de type INT avec une valeur par défaut de 1
-- <name VARCHAR(256)> Définit une colonne name de type VARCHAR avec une longueur maximale de 256 caractères
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
