// Sélectionne l'élément avec l'ID 'add_item'
const addItem = document.querySelector('#add_item');

// Ajoute un gestionnaire d'événements pour réagir au clic sur l'élément add_item
addItem.addEventListener('click', function() {
    // Crée un nouvel élément <li>
    const newItem = document.createElement('li');

    // Ajoute du texte à l'élément <li>
    newItem.textContent = 'Item';

    // Sélectionne l'élément <ul> avec la classe 'my_list'
    const myList = document.querySelector('.my_list');

    // Ajoute le nouvel élément <li> à l'élément <ul>
    myList.appendChild(newItem);
});
