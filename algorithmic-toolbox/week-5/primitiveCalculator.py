# Uses python3
import math
import sys

operations = ['mul_2', 'mul_3', 'add_1'];

def calculatePrevNumberForOperation(operation, number):
    if operation == 'mul_2' and number % 2 == 0:
        return int(number / 2)
    elif operation == 'mul_3' and number % 3 == 0:
        return int(number / 3)
    elif operation == 'add_1':
        return number - 1

    return math.inf


# Calculates a min number of operations needed for get user's number 
def minOperationNumber(operations, number):
    minNumberOfOperationsForNumbers = {
        1: {
            'min_operation': 0,
            'back': -1
        }
    }

    index = 2

    while index <= number:
        minNumberOfOperationsToGetCurrentNumber = math.inf
        optimalPrevNumber = math.inf

        for operation in operations:
            prevNumber = calculatePrevNumberForOperation(operation, index)

            if index > prevNumber:
                backNumberData = minNumberOfOperationsForNumbers[prevNumber]
                numberOfChanges = backNumberData['min_operation'] + 1

                if numberOfChanges < minNumberOfOperationsToGetCurrentNumber:
                    minNumberOfOperationsToGetCurrentNumber = numberOfChanges
                    optimalPrevNumber = prevNumber


        minNumberOfOperationsForNumbers[index] = {
            'min_operation': minNumberOfOperationsToGetCurrentNumber,
            'back': optimalPrevNumber
        }


        index = index + 1


    return minNumberOfOperationsForNumbers


if __name__ == '__main__':
    number = int(sys.stdin.read())

    print(minOperationNumber(operations, number))


