-- <SELECT> Sélectionne les noms des genres de l'émission de télévision et affiche le nombre correspondant.
-- <FROM> Spécifie la table source à partir de laquelle les données sont récupérées, ici tv_genres.
-- <JOIN> Effectue une jointure interne entre les tables tv_genres et tv_show_genres en utilisant tv_genres.id et tv_show_genres.genre_id.
-- <ON> Spécifie la condition de jointure, où tv_genres.id doit correspondre à tv_show_genres.genre_id.
-- <GROUP BY> Groupe les résultats par le nom du genre, de sorte que COUNT puisse être appliqué à chaque groupe distinct.
-- <ORDER BY> Trie les résultats en fonction du nombre de spectacles dans chaque genre, en ordre décroissant.
-- Import the database dump from hbtn_0d_tvshows.
SELECT tv_genres.name AS genre,  -- Sélectionne les noms des genres de l'émission de télévision et affiche le nombre correspondant.
       COUNT(tv_show_genres.show_id) AS number_of_shows  -- Calcule le nombre d'émissions de télévision associées à chaque genre.
FROM tv_genres  -- Spécifie la table source à partir de laquelle les données sont récupérées, ici tv_genres.
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- Effectue une jointure interne entre les tables tv_genres et tv_show_genres en utilisant tv_genres.id et tv_show_genres.genre_id.
GROUP BY tv_genres.name  -- Groupe les résultats par le nom du genre, de sorte que COUNT puisse être appliqué à chaque groupe distinct.
ORDER BY number_of_shows DESC;  -- Trie les résultats en fonction du nombre de spectacles dans chaque genre, en ordre décroissant.
