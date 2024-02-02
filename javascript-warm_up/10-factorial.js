#!/usr/bin/node
const args = process.argv.slice(2);
const integer = parseInt(args[0]);
if (isNaN(integer)) {
  console.log('1');
} else {
  let fact = 1;
  for (let i = 1; i <= integer; i++) {
    fact *= i;
  }
  console.log(fact);
}
