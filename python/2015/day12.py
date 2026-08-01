import json

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "12.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    line = [[char for char in line] for line in file][0]

    sumNums = 0
    num = ''
    for char in line:
        if char.isdigit() or (char == '-' and num == ''):
            num += char
        else:
            if num:
                sumNums += int(num)
                num = ''
    if num:
        sumNums += int(num)
    print(sumNums)


def partTwo():
    file = open(INPUT_FILE)
    data = json.load(file)

    def sumNums(obj):
        if isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            return sum(sumNums(v) for v in obj.values())
        elif isinstance(obj, list):
            return sum(sumNums(i) for i in obj)
        elif isinstance(obj, int):
            return obj
        return 0

    totalSum = sumNums(data)
    print(totalSum)


if __name__ == '__main__':
    main()