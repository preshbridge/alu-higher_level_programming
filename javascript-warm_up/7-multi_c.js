#!/usr/bin/node

const argNum = Number(process.argv[2]);

if (!Number.isNaN(argNum)) {
  for (let i = 0; i < argNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
