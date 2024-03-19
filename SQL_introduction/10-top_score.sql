-- <SELECT> les scores et les noms des enregistrements de la table "second_table"
SELECT score, name

-- <FROM> Extraire la base de données "hbtn_0c_0" à de la seconde colonne
FROM hbtn_0c_0.second_table

-- <ORDER BY> Trie les résultats par score, <DESC> permet en ordre décroissant.
ORDER BY score DESC;
