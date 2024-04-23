#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  fetchAndPrintCharacters(charactersUrls);
});

function fetchAndPrintCharacters(charactersUrls) {
  if (charactersUrls.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  let count = 0;
  charactersUrls.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Check if all characters have been printed
      count++;
      if (count === charactersUrls.length) {
        console.log('');
      }
    });
  });
}

