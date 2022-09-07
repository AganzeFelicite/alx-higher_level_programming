#!/usr/bin/node
/**
 * this is a factorial of a number
 * */
const num1 = parseInt(process.argv[2], 10);
const val = factorial(num1);
console.log(val);
function factorial (num) {
  if (num >= 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
