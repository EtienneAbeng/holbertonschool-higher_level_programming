-- <CREATE TABLE> Crée une nouvelle table dans la base de données si elle n'existe pas déjà
-- <UNIQUE> garantit qu'aucune valeur en double n'est autorisée dans la colonne où elle est appliquée
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,  -- Crée une colonne id de type INT avec une valeur par défaut de 1 et unique
    name VARCHAR(256) NOT NULL  -- Crée une colonne name de type VARCHAR avec une longueur maximale de 256 caractères, non nulle
);
