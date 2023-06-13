#!/usr/bin/node
/**
 * this converts a value to another base
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
