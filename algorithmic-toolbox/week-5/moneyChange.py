# Uses python3
import math
import sys

def moneyChange(coins, money):
    minNumberOfChangesForCoins = [0]

    index = 1

    while index <= money:
        minNumberOfChanges = math.inf

        for coin in coins:
            if index >= coin:
                numberOfChanges = minNumberOfChangesForCoins[index - coin] + 1

                if numberOfChanges < minNumberOfChanges:
                    minNumberOfChanges = numberOfChanges

        minNumberOfChangesForCoins.append(minNumberOfChanges)

        index = index + 1


    return minNumberOfChangesForCoins[money]


demonations = [1, 3, 4];


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(moneyChange(demonations, m))


