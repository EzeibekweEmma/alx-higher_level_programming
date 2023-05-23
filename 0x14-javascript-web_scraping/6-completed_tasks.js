#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const idData = {};

    data.forEach((isCompleted) => {
      if (isCompleted.completed) {
        idData[isCompleted.userId] = (idData[isCompleted.userId] || 0) + 1;
      }
    });
    console.log(idData);
  } else {
    console.log(err);
  }
});
