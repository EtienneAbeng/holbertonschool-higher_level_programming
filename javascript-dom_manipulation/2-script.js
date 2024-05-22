// Sélectionne l'élément avec l'ID 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément red_header
redHeader.addEventListener('click', function () {
  // Sélectionne l'élément <header>
  const header = document.querySelector('#red_header');

  // Ajoute la classe 'red' à l'élément <header>
  header.classList.add('red');
});
