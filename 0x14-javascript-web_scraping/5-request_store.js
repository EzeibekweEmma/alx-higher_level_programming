#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const { writeFile } = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    writeFile(path, body, 'utf-8', (err) => {
      if (err) console.log('Error writing to file:', err);
    });
  } else console.log(err);
});
