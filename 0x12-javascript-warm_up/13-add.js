#!/usr/bin/node
/* learning how to export modules in node */

exports.add = function (a, b) {
  return parseInt(a) + parseInt(b);
};
