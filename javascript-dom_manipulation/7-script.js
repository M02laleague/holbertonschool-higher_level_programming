fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Check if the response is okay and convert it to JSON
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Select the <ul> element with id 'list_movies'
    const listMovies = document.getElementById('list_movies');
    // Loop through each movie and create a <li> element with the movie title
    data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    // Log any errors to the console
    console.error('There was a problem with the fetch operation:', error);
});