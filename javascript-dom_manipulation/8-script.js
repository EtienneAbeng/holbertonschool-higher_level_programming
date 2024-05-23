// URL de l'API pour obtenir la traduction de "hello" en français
const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Fonction pour récupérer et afficher la traduction de "hello"
function fetchHello () {
  fetch(apiUrl)
    .then(response => response.json()) // Conversion de la réponse en JSON
    .then(data => {
      // Sélection de l'élément avec l'ID 'hello'
      const helloDiv = document.querySelector('#hello');

      // Mise à jour du contenu de l'élément avec la traduction de "hello"
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Erreur:', error)); // Gestion des erreurs
}

// Appel de la fonction pour récupérer et afficher la traduction de "hello"
document.addEventListener('DOMContentLoaded', fetchHello);
