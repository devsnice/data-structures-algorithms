const sumFibNumbersLastDigit = number => {
  let fibPrevPrevNumber = 0;
  let fibPrevNumber = 1;

  let sumOfFirstNFibNumbers = 0;

  if (number >= 1) {
    sumOfFirstNFibNumbers = fibPrevPrevNumber + fibPrevNumber;
  }

  for (i = 2; i <= number; i++) {
    let newNumber = (fibPrevPrevNumber + fibPrevNumber) % 10;

    fibPrevPrevNumber = fibPrevNumber;
    fibPrevNumber = newNumber;

    sumOfFirstNFibNumbers = (sumOfFirstNFibNumbers + newNumber) % 10;
  }

  return sumOfFirstNFibNumbers;
};
