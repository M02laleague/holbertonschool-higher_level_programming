const toggleHeader = document.getElementById('toggle_header');

// Add a click event listener to the selected element
toggleHeader.addEventListener('click', () => {
    // Select the <header> element
    const header = document.querySelector('header');
    
    // Toggle the class between 'red' and 'green'
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else if (header.classList.contains('green')) {
        header.classList.remove('green');
        header.classList.add('red');
    }
});