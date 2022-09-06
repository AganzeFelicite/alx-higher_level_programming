#!/usr/bin/node
/**
 * this is to print C is fun x time
 * x is the first argument of the
 * argv
 * */
const word = 'C is fun';
const val = parseInt(process.argv[2], 10);

if (val) {
  for (let i = 0; i <= val; i++) {
    console.log(word);
  }
} else {
  console.log('Missing number of occurrences');
}
