#!/usr/bin/node
/**
 * dealing with number
 * convesion in javascript
 * */

const number = parseInt(process.argv[2], 10);
if (number) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
