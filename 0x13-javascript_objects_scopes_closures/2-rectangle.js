#!/usr/bin/node
/**
 * this si a rectangle class defined this defines an empty obj if args are <= 0
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
