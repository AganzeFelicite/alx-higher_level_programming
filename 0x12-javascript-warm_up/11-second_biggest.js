#!/usr/bin/node
/**
 * a script that searches for the second biggest
 * integer in the list of arguments
 * */
function secondlast () {
  if (process.argv[2] === undefined || process.argv[3] === undefined) {
    console.log(0);
    return 0;
  }
  const array = process.argv;
  for (let i = 2; i <= array.length - 1; i++) {
    array[i] = parseInt(array[i]);
  }
  array.sort(function (a, b) { return b - a; });
  console.log(array[3]);
}

secondlast();
