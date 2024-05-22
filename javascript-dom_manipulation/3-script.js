// Sélectionne l'élément avec l'ID 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément toggle_header
toggleHeader.addEventListener('click', function () {
  // Sélectionne l'élément <header>
  const header = document.querySelector('header');

  // Toggle la classe 'red' sur l'élément <header>
  header.classList.toggle('red');

  // Toggle la classe 'green' sur l'élément <header>
  header.classList.toggle('green');
});
