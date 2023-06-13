#!/usr/bin/node
/**
 * this si a rectangle class defined this defines an empty obj if args are <= 0
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { console.log('X'.repeat(this.width)); }
    }
  }
}
module.exports = Rectangle;
