import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "1.txt"
def main():
    partOne()
    partTwo()

def partOne():
    file = open(INPUT_FILE)
    print(sum(line.count("(") - line.count(")") for line in file))

def partTwo():
    file = open(INPUT_FILE)
    floor = 0
    for line in file:
        for i in range(len(line)):
            if floor == -1:
                print(i)
                return
            if line[i] == "(":
                floor += 1
            else:
                floor -= 1

if __name__ == '__main__':
    main()