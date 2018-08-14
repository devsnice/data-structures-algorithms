/**
 * Find the greatest common divisor of two numbers
 *
 * @param {Number} a
 * @param {Number} b
 * @returns {Number} result
 */

function greatestCommonDivisor(a, b) {
  if (a === 0) {
    return b;
  }

  if (b === 0) {
    return a;
  }

  const remains = a % b;

  return greatestCommonDivisor(b, remains);
}
