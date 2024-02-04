#!/usr/bin/node
function factorial (n) {
  return isNaN(n) || n === 0 || n === 1 ? 1 : n * factorial(n - 1);
}

const arg = +process.argv[2];

console.log(factorial(arg));
