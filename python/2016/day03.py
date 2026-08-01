import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "3.txt"
def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    lines = [sorted([int(char.strip()) for char in line.strip().split(" ") if char.strip()]) for line in file]
    count = 0
    for line in lines:
        if line[0] + line[1] > line[2]:
            count += 1
    print(count)


def partTwo():
    file = open(INPUT_FILE)
    lines = [[int(char.strip()) for char in line.strip().split(" ") if char.strip()] for line in file]
    count = 0
    for i in range(0, len(lines), 3):
        for j in range(3):
            line = sorted([lines[i][j], lines[i + 1][j], lines[i + 2][j]])
            if line[0] + line[1] > line[2]:
                count += 1
    print(count)


if __name__ == '__main__':
    main()