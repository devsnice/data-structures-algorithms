# Uses python3

import sys

def knapsackGetElements(D, weights, capacity):
    currentElementIndex = len(weights)
    currentCapacity = capacity

    elements = []

    while currentElementIndex > 0:
        # в рюкзак взяли предыдущий рюкзак и не взяли текущий элемент
        if D[currentElementIndex][currentCapacity] == D[currentElementIndex - 1][currentCapacity]:
            currentElementIndex = currentElementIndex - 1
        else:
            elements.append(weights[currentElementIndex - 1])
            currentCapacity = currentCapacity - weights[currentElementIndex -1]
            currentElementIndex = currentElementIndex - 1

    return elements

def removeElementsUsedInKnapsack(array, knapsack):
  resultArray = [];
  deleted = [];

  for index in range(len(array)):
      if array[index] not in knapsack or array[index] in deleted:
          resultArray.append(array[index])
      else:
          deleted.append(array[index])
  
  return resultArray

def knapsackWithoutRepetitions(weights, capacity):
    D = {}

    for i in range(len(weights) + 1):
        D[i] = {}

        for j in range(0, capacity + 1):
            D[i][j] = 0

    sets = []

    # считаем все возможные варианты для выборки элементов 1...capacity
    # для каждого размера рюкзака
    for forElementAmount in range(1, len(weights) + 1):
        for forCapacity in range(1, capacity + 1):
            # берём предыдущий рюкзак, считаем его оптимальным
            D[forElementAmount][forCapacity] = D[forElementAmount-1][forCapacity]

            # если элемент возможно положить в рюкзак
            if weights[forElementAmount - 1] <= forCapacity:
                tryToPutCurrentElement = D[forElementAmount-1][forCapacity - weights[forElementAmount - 1]] + weights[forElementAmount - 1]

                # пытаемся положить в рюкзак меньше размера текущий элемент
                if tryToPutCurrentElement <= forCapacity:
                    if tryToPutCurrentElement >= D[forElementAmount][forCapacity]:
                        D[forElementAmount][forCapacity] = tryToPutCurrentElement

    # модификация, проверям, можно ли заполнить рюкзак полностью
    if D[len(weights)][capacity] != capacity:
        return 0

    # возвращаем, что нужно положить в рюкзак
    return knapsackGetElements(D, weights, capacity)


def partition3(array):
    array.sort(reverse=True)

    if len(array) < 3:
        return 0

    sum = 0;

    for index in range(len(array)):
        sum = sum + array[index]

    if sum % 3 != 0:
        return 0

    thirdPart = sum // 3

    firstKnapsack = knapsackWithoutRepetitions(array, thirdPart)

    if firstKnapsack == 0:
        return 0

    arrayWithoutFirstKnapsack = removeElementsUsedInKnapsack(array, firstKnapsack)

    secondKnapsack = knapsackWithoutRepetitions(arrayWithoutFirstKnapsack, thirdPart)

    if secondKnapsack == 0:
        return 0

    return 1

if __name__ == "__main__":
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))