import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "10.txt"
def main():
    partOne()
    partTwo()


def lookAndSay(sequence):
    result = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + sequence[i])
        i += 1
    return ''.join(result)


def partOne():
    file = open(INPUT_FILE)
    line = [char for char in file.readline().strip()]
    for _ in range(40):
        line = lookAndSay(line)

    print(len(line))


def partTwo():
    file = open(INPUT_FILE)
    line = [char for char in file.readline().strip()]
    for _ in range(50):
        line = lookAndSay(line)

    print(len(line))


if __name__ == '__main__':
    main()