#!/usr/bin/node
function factorial (integer) {
  if (isNaN(integer)) {
    return 1;
  }
  if (integer === 1) {
    return 1;
  }
  return integer * factorial(integer - 1);
}
const args = process.argv.slice(2);
const integer = parseInt(args[0]);
console.log(factorial(integer));
