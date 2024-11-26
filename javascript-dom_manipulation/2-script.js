document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header');
    header.addEventListener('click', () => {
        header.classList.add('red');
    });
});