// Sélectionne l'élément avec l'ID 'update_header'
const updateHeader = document.querySelector('#update_header');
// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément update_header
updateHeader.addEventListener('click', function() {
  // Sélectionne l'élément <header>
  const header = document.querySelector('header');
  // Met à jour le texte de l'élément <header>
  header.textContent = 'New Header!!!';
});
