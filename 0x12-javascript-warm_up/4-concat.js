#!/usr/bin/node
/**
 * concatination of
 * argv values
 *
 * */

let word;
if (process.argv[2]) {
  word = process.argv[2] + ' is ' + process.argv[3];
  console.log(word);
}
