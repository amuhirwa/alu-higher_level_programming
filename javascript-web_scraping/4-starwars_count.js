#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedData = JSON.parse(body);
    const results = parsedData.results;
    const counts = results.filter(i => /people\/18/.test(i.characters)).length;
    console.log(counts);
  }
});
