//  script that adds a <li> element to a list when the user clicks on the element with id add_item

let button = document.getElementById('add_item');
button.addEventListener('click', function() {
    let MyList = document.querySelector('.my_list');
    let ElementToAdd = document.createElement('li');
    ElementToAdd.textContent = 'Item';
    MyList.appendChild(ElementToAdd);
});