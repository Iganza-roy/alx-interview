#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// base API url
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie: ${response.statusCode}`);
    return;
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  //   getting the list of character URLs
  characters.forEach((url) => {
    request(url, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error('Error:', charErr);
        return;
      }
      if (charRes.statusCode !== 200) {
        console.error(`Failed to fetch character: ${charRes.statusCode}`);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
