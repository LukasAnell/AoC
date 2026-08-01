import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "19.txt"
def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    numElves = int([line.strip() for line in file][0])
    elves = [(i, 1) for i in range(1, numElves + 1)]
    while len(elves) > 1:
        for i in range(len(elves)):
           pass


def partTwo():
    pass


if __name__ == "__main__":
    main()
