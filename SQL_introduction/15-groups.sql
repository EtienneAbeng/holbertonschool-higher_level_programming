-- <SELECT> Sélectionne le score et compte le nombre d'enregistrements pour chaque score
SELECT score, COUNT(*) AS number

-- <FROM> Extrait les données de la table "second_table" de la base de données "hbtn_0c_0"
FROM second_table

-- <GROUP BY> Regroupe les enregistrements par score et compte le nombre d'enregistrements pour chaque score
GROUP BY score

-- <ORDER BY> Trie les résultats par le nombre d'enregistrements (en ordre décroissant)
ORDER BY number DESC;
