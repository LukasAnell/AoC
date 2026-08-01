import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "8.txt"
def main():
    partOne()
    partTwo()

def partOne():
    file = open(INPUT_FILE)
    codeCount = 0
    memoryCount = 0
    for line in file:
        line = line.strip()
        codeCount += len(line)
        memoryCount += len(eval(line))
    print(codeCount - memoryCount)


def partTwo():
    file = open(INPUT_FILE)
    originalCount = 0
    encodedCount = 0
    for line in file:
        line = line.strip()
        originalCount += len(line)
        encodedLine = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        encodedCount += len(encodedLine)
    print(encodedCount - originalCount)


if __name__ == '__main__':
    main()