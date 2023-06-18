#!/usr/bin/node
/**
 * this multiplies each item in the list by its index:x
 *
 */
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
