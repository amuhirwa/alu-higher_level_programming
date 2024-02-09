#!/usr/bin/node
const fs = require('fs');
const path = process.args.slice(2)[0];
fs.readFile(path, (err, data) => {
  console.log(err);
});
