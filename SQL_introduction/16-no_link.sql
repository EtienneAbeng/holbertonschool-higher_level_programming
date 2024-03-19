-- <SELECT> Sélectionne le score et le nom des enregistrements de la table "second_table"
SELECT score, name

-- <FROM> Extrait les données de la table "second_table" de la base de données "hbtn_0c_0"
FROM hbtn_0c_0.second_table

-- <WHERE> Filtre les enregistrements pour inclure uniquement ceux avec un nom non nul
WHERE name IS NOT NULL

-- <ORDER BY> Trie les résultats par score en ordre décroissant
ORDER BY score DESC;
