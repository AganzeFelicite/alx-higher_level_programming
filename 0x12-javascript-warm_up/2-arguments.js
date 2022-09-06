#!/usr/bin/node
/***
 * this is to print aargvs
 */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
