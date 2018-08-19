const largeFibNumberLastSign = number => {
  const fibTable = {
    0: 0,
    1: 1
  };

  for (i = 2; i <= number; i++) {
    fibTable[i] = (fibTable[i - 1] + fibTable[i - 2]) % 10;
  }

  return fibTable[number];
};
