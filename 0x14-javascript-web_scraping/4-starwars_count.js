#!/usr/bin/node
// Write a script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body).results;

    let count = 0;
    data.forEach((film) => {
      const characters = film.characters;
      if (
        characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterId}/`
        )
      ) {
        count++;
      }
    });

    console.log(count);
  }
});
