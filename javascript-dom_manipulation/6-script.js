fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        // Check if the response is okay and convert it to JSON
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Select the element with id 'character' and update its content
        document.getElementById('character').textContent = data.name;
    })
    .catch(error => {
        // Log any errors to the console
        console.error('There was a problem with the fetch operation:', error);
    });