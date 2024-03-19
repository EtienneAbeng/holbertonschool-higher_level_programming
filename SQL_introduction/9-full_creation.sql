-- Crée une nouvelle table de données et ajoute des lignes en entrée

CREATE TABLE IF NOT EXISTS second_table(
    id INT,  -- Colonne identifiant de l'enregistrement
    name VARCHAR(256),  -- Colonne nom
    score INT  -- Colonne score
);

-- Ajoute des enregistrements à la table second_table
INSERT INTO second_table (id, name, score)

VALUES 
    (1, 'John', 10),    -- Enregistrement avec id=1, name='John' et score=10
    (2, 'Alex', 3),     -- Enregistrement avec id=2, name='Alex' et score=3
    (3, 'Bob', 14),     -- Enregistrement avec id=3, name='Bob' et score=14
    (4, 'George', 8);   -- Enregistrement avec id=4, name='George' et score=8
