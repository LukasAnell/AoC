import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2015" / "16.txt"
def main():
    message = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    partOne(message)
    partTwo(message)


def getSueList():
    file = open(INPUT_FILE)
    sueList = []
    for line in file:
        parts = line.strip().split(": ", 1)
        sue = {"number": int(parts[0].split(" ")[1])}
        attributes = parts[1].split(", ")
        for attribute in attributes:
            key, value = attribute.split(": ")
            sue[key] = int(value)
        sueList.append(sue)
    return sueList


def partOne(message):
    sueList = getSueList()
    for sue in sueList:
        match = True
        for key,value in sue.items():
            if key == "number":
                continue
            if key in message and message[key] != value:
                match = False
                break
        if match:
            print(sue["number"])
            break


def partTwo(message):
    sueList = getSueList()
    for sue in sueList:
        match = True
        for key, value in sue.items():
            if key == "number":
                continue
            if key in message:
                if key in ["cats", "trees"]:
                    if message[key] >= value:
                        match = False
                        break
                elif key in ["pomeranians", "goldfish"]:
                    if message[key] <= value:
                        match = False
                        break
                else:
                    if message[key] != value:
                        match = False
                        break
        if match:
            print(sue["number"])
            break


if __name__ == '__main__':
    main()