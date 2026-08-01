import itertools

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "9.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    connectionMap = {}
    locations = set()
    for line in file:
        splitLine = line.strip().split(" ")
        start = splitLine[0]
        end = splitLine[2]
        distance = int(splitLine[4])
        connectionMap[(start, end)] = distance
        connectionMap[(end, start)] = distance
        locations.add(start)
        locations.add(end)

    shortestRoute = float('inf')

    for route in itertools.permutations(locations):
        totalDistance = sum(connectionMap[(route[i], route[i + 1])] for i in range(len(route) - 1))
        if totalDistance < shortestRoute:
            shortestRoute = totalDistance

    print(shortestRoute)

def partTwo():
    file = open(INPUT_FILE)
    connectionMap = {}
    locations = set()
    for line in file:
        splitLine = line.strip().split(" ")
        start = splitLine[0]
        end = splitLine[2]
        distance = int(splitLine[4])
        connectionMap[(start, end)] = distance
        connectionMap[(end, start)] = distance
        locations.add(start)
        locations.add(end)

    longestRoute = 0

    for route in itertools.permutations(locations):
        totalDistance = sum(connectionMap[(route[i], route[i + 1])] for i in range(len(route) - 1))
        if totalDistance > longestRoute:
            longestRoute = totalDistance

    print(longestRoute)


if __name__ == '__main__':
    main()