#!/usr/bin/node
/**
 * this is to print the first argument pass to it
 **/

if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
