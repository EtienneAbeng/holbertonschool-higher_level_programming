// Sélectionne l'élément avec l'ID 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément red_header
redHeader.addEventListener('click', function () {
  // Sélectionne l'élément <header> s'il existe
  const header = document.querySelector('header');
  
  // Vérifie si l'élément <header> existe et que la classe 'red' n'est pas déjà présente
  if (header && !header.classList.contains('red')) {
    // Ajoute la classe 'red' à l'élément <header>
    header.classList.add('red');
  }
});
