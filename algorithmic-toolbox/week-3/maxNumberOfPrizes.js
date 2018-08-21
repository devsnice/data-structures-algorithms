/**
 * Its function represent a given number n as a sum of as many pairwise distinct positive integers as possible
 * @param {Number} n
 */
const maxNumberOfPrizes = n => {
  const result = [];
  let i = 1;
  let sum = 0;

  while (sum < n) {
    let restSumAfterThisSolution = n - sum - i;

    // It's the same as below, but it use a lot memory
    // let nextStepWillRepeatNumber = [...result, i].includes(
    //   restSumAfterThisSolution
    // );

    let nextStepWillRepeatNumber = result.includes(restSumAfterThisSolution);

    if (!nextStepWillRepeatNumber && i !== restSumAfterThisSolution) {
      result.push(i);
      sum += i;
    }

    i++;
  }

  console.log(result.length);
  console.log(result.join(" "));
};
