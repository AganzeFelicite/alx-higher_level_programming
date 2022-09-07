#!/usr/bin/node
/**
 * a script that searches for the second biggest
 * integer in the list of arguments
 * */
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
}
let large = parseInt(process.argv[2]);
let secondlarge = 0;
const array = process.argv;
for (let i = 2; i < array.length; i++) {
  if (parseInt(array[i]) > large) {
    secondlarge = large;
    large = parseInt(array[i]);
  } else if (parseInt(array[i]) > secondlarge && array.length > 3) {
    secondlarge = parseInt(array[i]);
  }
}
console.log(secondlarge);
