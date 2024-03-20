-- <SELECT> Sélectionne toutes les villes de la table cities
SELECT * FROM cities
-- <WHERE> Filtrer les résultats où l'état de la ville est égal à l'ID de l'état de Californie
WHERE state_id = (
    -- <SELECT> Sélectionne l'ID de l'état de Californie de la table states
    SELECT id FROM states WHERE name = 'California'
)
-- <ORDER BY> Trie les résultats par ordre croissant en fonction de l'ID de la ville
ORDER BY id ASC;
