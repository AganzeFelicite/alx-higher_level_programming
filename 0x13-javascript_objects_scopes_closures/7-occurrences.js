#!/usr/bin/node
/**
 * this is a function that return the
 * number of a search item in a array
 */

exports.nbOccurences = function (list, searchElement) {
  let counts = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counts++;
    }
  }
  return counts;
};
