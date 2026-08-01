import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "3.txt"
def main():
    partOne()
    partTwo()

def partOne():
    file = open(INPUT_FILE)
    visitedMap = [(0, 0)]
    directions = [[char for char in line] for line in file][0]
    i, j = 0, 0
    for char in directions:
        if char == '^': i -= 1
        if char == '>': j += 1
        if char == 'v': i += 1
        if char == '<': j -= 1

        if (i, j) not in visitedMap:
            visitedMap.append((i, j))
    print(len(visitedMap))

def partTwo():
    file = open(INPUT_FILE)
    santaVisited = [(0, 0)]
    roboSantaVisited = []
    directions = [[char for char in line] for line in file][0]
    i, j = 0, 0
    r, c = 0, 0
    roboSanta = False
    for char in directions:
        if roboSanta:
            if char == '^': r -= 1
            if char == '>': c += 1
            if char == 'v': r += 1
            if char == '<': c -= 1

            if (r, c) not in santaVisited:
                santaVisited.append((r, c))
        else:
            if char == '^': i -= 1
            if char == '>': j += 1
            if char == 'v': i += 1
            if char == '<': j -= 1

            if (i, j) not in santaVisited:
                santaVisited.append((i, j))
        roboSanta = not roboSanta
    print(len(santaVisited) + len(roboSantaVisited))

if __name__ == '__main__':
    main()