/**
 *  The goal in this problem is to find the minimum number of coins
 *  needed to change the input value (an integer)
 * into coins with denominations 1, 5, and 10.
 */

// Greedy solution - slow version
const moneyChange = function(money) {
  // works for any nominals
  const nominals = [10, 5, 1];
  let numberOfCoins = 0;

  const denominations = (amount, nominal) => {
    while (amount !== 0) {
      if (amount - nominal >= 0) {
        numberOfCoins += 1;
        amount = amount - nominal;
      } else {
        if (nominals.length !== 0) {
          let nextNominal = nominals.shift();

          return denominations(amount, nextNominal);
        }
      }
    }

    return numberOfCoins;
  };

  return denominations(money, nominals.shift());
};

module.exports = moneyChange;
