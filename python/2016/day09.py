import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "9.txt"
def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    line = [line.strip() for line in file][0]
    decompressedLength = 0
    i = 0
    while i < len(line):
        if line[i] == '(':
            i += 1
            marker = ""
            while line[i] != ')':
                marker += line[i]
                i += 1
            i += 1
            marker = marker.split('x')
            length = int(marker[0])
            repeat = int(marker[1])
            decompressedLength += length * repeat
            i += length
        else:
            decompressedLength += 1
            i += 1
    print(decompressedLength)


def decompressedExtra(line):
    decompressedLength = 0
    i = 0
    while i < len(line):
        if line[i] == '(':
            i += 1
            marker = ""
            while line[i] != ')':
                marker += line[i]
                i += 1
            i += 1
            marker = marker.split('x')
            sub_length = int(marker[0])
            repeat = int(marker[1])
            decompressedLength += repeat * decompressedExtra(line[i:i + sub_length])
            i += sub_length
        else:
            decompressedLength += 1
            i += 1
    return decompressedLength


def partTwo():
    file = open(INPUT_FILE)
    print(decompressedExtra([line.strip() for line in file][0]))


if __name__ == '__main__':
    main()