/**
 * Compose a large number from numbers
 * @param {Array} stringNumbers
 */
const maxSalary = stringNumbers => {
  // sort elements in such order,
  // that in the first place will a number,
  // which makes a large number from all sequence
  const sortedNumbers = stringNumbers.sort((a, b) => {
    // 21, 2 -> 212 < 221 -> 221 -> 2 should be less that 21
    if (a + b < b + a) {
      return 1;
    } else return -1;
  });

  console.log(sortedNumbers.join(""));
};
