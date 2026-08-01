import functools

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2024" / "1.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    left, right = (sorted(list(x)) for x in zip(*[(int(pair[0]), int(pair[1])) for pair in [line.strip().split("   ") for line in file]]))
    print(sum(abs(x - y) for x, y in zip(left, right)))


@functools.cache
def partTwo():
    file = open(INPUT_FILE)
    left, right = (list(x) for x in zip(*[(int(pair[0]), int(pair[1])) for pair in [line.strip().split("   ") for line in file]]))
    print(sum(num * right.count(num) for num in left))


if __name__ == '__main__':
    main()