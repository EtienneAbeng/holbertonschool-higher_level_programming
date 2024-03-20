-- <SELECT> Sélectionne les informations nécessaires pour chaque ville
SELECT cities.id, cities.name, states.name
-- <FROM> Spécifie les tables à partir desquelles nous obtenons les données
FROM cities
-- <JOIN> Jointure avec la table des états pour obtenir le nom de l'état pour chaque ville
JOIN states ON cities.state_id = states.id
-- <ORDER BY> Trie les résultats par ordre croissant selon l'ID de la ville
ORDER BY cities.id ASC;
