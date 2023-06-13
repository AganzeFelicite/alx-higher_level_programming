#!/usr/bin/node
/**
 * this is a function that reverse an array
 */

exports.esrever = function (list) {
  const arr = [];
  for (let i = list.length; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
