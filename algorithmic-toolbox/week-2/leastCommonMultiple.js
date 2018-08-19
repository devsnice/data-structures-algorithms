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

function leastCommonMultiple(a, b) {
  return (a / greatestCommonDivisor(a, b)) * b;
}
