# Uses python3

import sys

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

    return len(weights)][capacity]:
        return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    print(knapsackWithoutRepetitions(w, W))