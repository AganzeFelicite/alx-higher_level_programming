#!/usr/bin/node
/**
 * this a square class that inherits from Rectangle of 4-rectangle.js
 * You must use the class notation for defining your class and extends
 *
 */

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
