import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "1.txt"
def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    lines = [line.strip() for line in file][0].split(", ")
    pos = 0,0
    facing = 0,1
    for instruction in lines:
        direction, distance = instruction[0], instruction[1:]
        if direction == 'L':
            facing = facing[1], -facing[0]
        else:
            facing = -facing[1], facing[0]
        pos = pos[0] + facing[0]*int(distance), pos[1] + facing[1]*int(distance)
    print(abs(pos[0]) + abs(pos[1]))


def partTwo():
    file = open(INPUT_FILE)
    lines = [line.strip() for line in file][0].split(", ")
    pos = 0,0
    facing = 0,1
    visited = set()
    for instruction in lines:
        direction, distance = instruction[0], instruction[1:]
        if direction == 'L':
            facing = facing[1], -facing[0]
        else:
            facing = -facing[1], facing[0]
        for i in range(int(distance)):
            pos = pos[0] + facing[0], pos[1] + facing[1]
            if pos in visited:
                print(abs(pos[0]) + abs(pos[1]))
                return
            visited.add(pos)


if __name__ == '__main__':
    main()