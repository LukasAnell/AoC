import operator
from functools import reduce

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "2.txt"


def main():
    partOne()
    partTwo()

def partOne():
    file = open(INPUT_FILE)
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
    file = open(INPUT_FILE)
    squareFeet = 0
    for line in file:
        dimensions = sorted([int(num) for num in line.split("x")])
        squareFeet += 2 * (dimensions[0] + dimensions[1]) + reduce(operator.mul, dimensions)
    print(squareFeet)

if __name__ == '__main__':
    main()