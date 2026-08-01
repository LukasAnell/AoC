import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "16.txt"
def main():
    partOne()
    partTwo()


def getInitialState():
    file = open(INPUT_FILE)
    return [line.strip() for line in file][0]


def calculateChecksum(state, goalLength):
    while len(state) < goalLength:
        state = state + '0' + ''.join(['1' if c == '0' else '0' for c in state[::-1]])
    checksum = state[:goalLength]
    while len(checksum) % 2 == 0:
        checksum = ''.join(['1' if checksum[i] == checksum[i+1] else '0' for i in range(0, len(checksum), 2)])
    return checksum


def partOne():
    goalLength = 272
    print(calculateChecksum(getInitialState(), goalLength))


def partTwo():
    goalLength = 35651584
    print(calculateChecksum(getInitialState(), goalLength))


if __name__ == '__main__':
    main()
