-- <SELECT> Sélectionne les scores et les noms des enregistrements de la table "second_table"
SELECT score, name

-- <FROM> Extrait les données de la table "second_table" de la base de données "hbtn_0c_0"
FROM hbtn_0c_0.second_table

-- <WHERE> Filtre les enregistrements pour inclure uniquement ceux avec un score >= 10
WHERE score >= 10

-- <ORDER BY> Trie les résultats par score en ordre décroissant (du plus élevé au plus bas)
ORDER BY score DESC;
