#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const text = process.argv[3];

const write = fs.writeFile(path, text, 'utf-8', (err) => {
  if (err) {
    return err;
  }
});

console.log(write);
