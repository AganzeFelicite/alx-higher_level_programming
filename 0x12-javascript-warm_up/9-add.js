#!/usr/bin/node
/** add two number
 * */

function add (a, b) {
  return a + b;
}
const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);
if (num1 && num2) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
