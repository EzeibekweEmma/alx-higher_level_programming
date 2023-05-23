#!/usr/bin/node
// Write a script that writes a string to a file.

const fs = require('fs');
const path = process.argv[2];
const text = process.argv[3];

fs.writeFile(path, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
