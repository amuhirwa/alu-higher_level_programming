#!/usr/bin/node
const args = process.argv.slice(2);
const sorted = args.sort((a, b) => a - b);
console.log(sorted[sorted.length - 2]);
