#!/usr/bin/node
/**
 * this a square class that inherits from Rectangle of 4-rectangle.js
 * You must use the class notation for defining your class and extends
 *
 */

const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
