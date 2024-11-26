fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
        // Check if the response is okay and convert it to JSON
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Select the element with id 'hello' and update its content
        document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
        // Log any errors to the console
        console.error('There was a problem with the fetch operation:', error);
    });