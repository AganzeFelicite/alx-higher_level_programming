#!/usr/bin/node
/**
 * this is about a square
 * */
const str = 'X';
const num = parseInt(process.argv[2], 10);
if (num) {
  for (let i = 1; i <= num; i++) {
    console.log(str.repeat(num));
  }
} else {
  console.log('Missing size');
}
