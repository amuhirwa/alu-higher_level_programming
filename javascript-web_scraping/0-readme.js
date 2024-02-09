#!/usr/bin/node
const fs = require('fs');
const path = process.argv.slice(2)[0];
fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
