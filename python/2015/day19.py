from collections import deque

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "19.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    replacements = []
    starting = ""
    for line in file:
        line = line.strip()
        if "=>" in line:
            split = line.split(" => ")
            replacements.append((split[0], split[1]))
        elif line:
            starting = line
    distinct = set()
    for i in range(len(starting)):
        for old, new in replacements:
            if starting[i:i + len(old)] == old:
                newMolecule = starting[:i] + new + starting[i + len(old):]
                distinct.add(newMolecule)
    print(len(distinct))


def partTwo():
    file = open(INPUT_FILE)
    replacements = []
    target = ""
    for line in file:
        line = line.strip()
        if "=>" in line:
            split = line.split(" => ")
            replacements.append((split[1], split[0]))
        elif line:
            target = line
    elements = sum(1 for c in target if c.isupper())
    rnArCount = target.count("Rn") + target.count("Ar")
    yCount = target.count("Y")
    print(elements - rnArCount - 2 * yCount - 1)


if __name__ == '__main__':
    main()