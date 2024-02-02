#!/usr/bin/node
const args = process.argv.slice(2);
const integer = parseInt(args[0]);
if (isNaN(integer)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < integer; i++) {
    console.log('X'.repeat(integer));
  }
}
