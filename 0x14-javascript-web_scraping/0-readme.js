#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', (err, body) => {
  return console.log(err || body);
});