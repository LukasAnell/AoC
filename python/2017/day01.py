import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2017" / "1.txt"
def main():
    partOne()
    partTwo()


def partOne():
    line = [[int(digit) for digit in line.strip()] for line in open(INPUT_FILE)][0]
    sumDigits = 0
    for i in range(len(line) - 1):
        currentDigit, nextDigit = line[i], line[i + 1]
        if currentDigit == nextDigit:
            sumDigits += currentDigit
    if line[0] == line[-1]:
        sumDigits += line[0]
    print(sumDigits)


def partTwo():
    line = [[int(digit) for digit in line.strip()] for line in open(INPUT_FILE)][0]
    sumDigits = 0
    for i in range(len(line)):
        currentDigit, aroundDigit = line[i], line[(i + len(line) // 2) % len(line)]
        if currentDigit == aroundDigit:
            sumDigits += currentDigit
    print(sumDigits)


if __name__ == '__main__':
    main()
