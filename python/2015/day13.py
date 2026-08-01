from itertools import permutations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "13.txt"


def main():
    partOne()
    partTwo()


def getHappinessMap():
    file = open(INPUT_FILE)
    lines = [line.strip().split() for line in file]
    happinessMap = {}
    for line in lines:
        firstName = line[0]
        otherName = line[-1][:-1]
        happiness = int(line[3]) if line[2] == "gain" else -int(line[3])
        happinessMap[firstName] = happinessMap.get(firstName, []) + [(otherName, happiness)]
    return happinessMap


def calculateHappiness(arrangement, happinessMap):
    totalHappiness = 0
    for i in range(len(arrangement)):
        person = arrangement[i]
        leftNeighbor = arrangement[i - 1]
        rightNeighbor = arrangement[(i + 1) % len(arrangement)]
        totalHappiness += next(h for n, h in happinessMap[person] if n == leftNeighbor)
        totalHappiness += next(h for n, h in happinessMap[person] if n == rightNeighbor)
    return totalHappiness


def findOptimalSeating(happinessMap):
    people = list(happinessMap.keys())
    maxHappiness = float('-inf')
    for arrangement in permutations(people):
        happiness = calculateHappiness(arrangement, happinessMap)
        if happiness > maxHappiness:
            maxHappiness = happiness
    return maxHappiness


def partOne():
    happinessMap = getHappinessMap()
    print(findOptimalSeating(happinessMap))


def partTwo():
    happinessMap = getHappinessMap()
    people = list(happinessMap.keys())
    for person in people:
        happinessMap[person].append(("Me", 0))
        happinessMap["Me"] = happinessMap.get("Me", []) + [(person, 0)]
    print(findOptimalSeating(happinessMap))


if __name__ == '__main__':
    main()