// URL de l'API
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Utilisation de l'API Fetch pour obtenir les données
fetch(apiUrl)
  .then(response => response.json()) // Conversion de la réponse en JSON
  .then(data => {
    // Sélection de l'élément <ul> avec l'ID 'list_movies'
    const listMovies = document.querySelector('#list_movies');

    // Parcours des résultats et création des éléments <li> pour chaque film
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => console.error('Erreur:', error)); // Gestion des erreurs
