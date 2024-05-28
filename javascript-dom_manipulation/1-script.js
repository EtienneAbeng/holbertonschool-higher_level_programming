// Sélectionne l'élément avec l'ID 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément red_header
redHeader.addEventListener('click', function () {
  // Sélectionne l'élément <header>
  const header = document.querySelector('header');

  // Change la couleur du texte de l'élément <header> en rouge (#FF0000)
  header.style.color = '#FF0000';
});
