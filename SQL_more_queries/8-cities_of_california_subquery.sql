-- Active: 1710860491090@@127.0.0.1@3306@hbtn_0d_usa
-- lists all the cities of California that can be found.
SELECT id, name
FROM cities
-- <WHERE> Filtrer les villes où l'ID de l'état correspond à celui de la Californie
WHERE state_id = (
    -- <SELECT> Sélectionner l'ID de l'état de Californie de la table states
    SELECT id
    FROM states
    -- <WHERE> Filtrer les états où le nom est 'California'
    WHERE name = 'California')
-- <ORDER BY> Trier les résultats par ordre croissant en fonction de l'ID de la ville
ORDER BY id ASC;
