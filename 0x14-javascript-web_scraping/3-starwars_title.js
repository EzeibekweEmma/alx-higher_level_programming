#!/usr/bin/Node

const request = require('request');
const id = process.argv[2];

request.get(
  {
    url: `https://swapi-api.alx-tools.com/api/films/${id}`
  },
  (err, res, body) => {
    console.log(err || JSON.parse(body).title);
  }
);
