-- <CREATE TABLE> Crée une table nommée force_name si elle n'existe pas déjà
CREATE TABLE 
    IF NOT EXISTS force_name (
        id INT,  -- Identifiant de la force
        name VARCHAR(256) NOT NULL  -- Nom de la force (non nul)
);
