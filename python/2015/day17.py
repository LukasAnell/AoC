import itertools

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "17.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    containers = [int(line.strip()) for line in file]
    target = 150
    count = 0
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == target:
                count += 1
    print(count)


def partTwo():
    file = open(INPUT_FILE)
    containers = [int(line.strip()) for line in file]
    target = 150
    validCombinations = []
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == target:
                validCombinations.append(combination)
    minContainers = min(len(combination) for combination in validCombinations)
    minCombinationsCount = sum(1 for combination in validCombinations if len(combination) == minContainers)
    print(minCombinationsCount)


if __name__ == '__main__':
    main()