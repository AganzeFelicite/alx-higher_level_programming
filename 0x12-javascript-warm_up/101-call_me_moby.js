#!/usr/bin/node
/*this is a function that execute x timea
 */

exports.callMeMoby = function (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
}	
