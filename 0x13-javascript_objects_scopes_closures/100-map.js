#!/usr/bin/node
/**
 * this multiplies each item in the list by its index:x
 *
 */
const list = require('./101-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
