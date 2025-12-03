import operator
from functools import reduce


def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/2.txt", "r")
    squareFeet = 0
    for line in file:
        dimensions = [int(num) for num in line.split("x")]
        for i in range(len(dimensions)):
            for j in range(len(dimensions)):
                if i != j:
                    squareFeet += dimensions[i] * dimensions[j]
        squareFeet += sorted(dimensions)[0] * sorted(dimensions)[1]
    print(squareFeet)

def partTwo():
    file = open("Inputs/2.txt", "r")
    squareFeet = 0
    for line in file:
        dimensions = sorted([int(num) for num in line.split("x")])
        squareFeet += 2 * (dimensions[0] + dimensions[1]) + reduce(operator.mul, dimensions)
    print(squareFeet)

if __name__ == '__main__':
    main()