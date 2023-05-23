#!/usr/bin/Node

const request = require('request');
const url = process.argv[2];

request(
  {
    url: url
  },
  (err, res, body) => {
    console.log(`code: ${err || res.statusCode}`);
  }
);
