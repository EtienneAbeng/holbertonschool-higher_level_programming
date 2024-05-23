// URL de l'API
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Utilisation de l'API Fetch pour obtenir les données
fetch(apiUrl)
    // Conversion de la réponse en JSON
    .then(response => response.json())
    .then(data => {
        // Sélection de l'élément avec l'ID 'character'
        const characterDiv = document.querySelector('#character');
        
        // Mise à jour du contenu de l'élément avec le nom du personnage
        characterDiv.textContent = data.name;
    })
    .catch(error => console.error('Erreur:', error)); // Gestion des erreurs
