#!/usr/bin/env node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the base URL for the Star Wars API films endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch movie details and character names
function fetchMovieCharacters () {
  // Fetch the movie details
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie:', error);
      return;
    }
    const characters = JSON.parse(body).characters;

    // Function to fetch and print character details
    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error fetching character:', error);
            reject(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
            resolve();
          }
        });
      });
    };

    // Fetch each character's details sequentially
    (async () => {
      try {
        for (const characterUrl of characters) {
          await fetchCharacter(characterUrl);
        }
      } catch (error) {
        console.error('Error fetching character details:', error);
      }
    })();
  });
}

// Call the function to fetch movie characters
fetchMovieCharacters();
