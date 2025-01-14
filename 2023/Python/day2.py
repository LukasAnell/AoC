import math


def main():
    partOne()
    partTwo()


def getLinesParsed():
    file = open("Inputs/2.txt", "r")
    lines = [[[(int(value.split(" ")[0]), value.split(" ")[1]) for value in subset.split(", ")] for subset in
              line.strip().split(": ")[1].split("; ")] for line in file]
    return lines


def partOne():
    maxColorCounts = {
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }
    lines = getLinesParsed()
    idSum = 0
    for i, line in enumerate(lines):
        colorCounts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for subset in line:
            for value, color in subset:
                colorCounts[color] = max(colorCounts[color], value)
        if all(value <= maxColorCounts[color] for (color, value) in colorCounts.items()):
            idSum += i + 1
    print(idSum)


def partTwo():
    lines = getLinesParsed()
    powerSum = 0
    for i, line in enumerate(lines):
        colorCounts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for subset in line:
            for value, color in subset:
                colorCounts[color] = max(colorCounts[color], value)
        powerSum += math.prod(colorCounts.values())
    print(powerSum)


if __name__ == '__main__':
    main()