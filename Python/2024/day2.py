def main():
    partOne()
    partTwo()


def sortedAndDifference(line):
    isSorted = (all(line[i] < line[i + 1] for i in range(len(line) - 1))
                or all(line[i] > line[i + 1] for i in range(len(line) - 1)))
    difference = all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))
    return isSorted and difference


def partOne():
    file = open("Inputs/2.txt", "r")
    lines = [[int(char) for char in line.strip().split(" ")] for line in file]
    safeCount = 0
    for line in lines:
        if sortedAndDifference(line):
            safeCount += 1
    print(safeCount)


def partTwo():
    file = open("Inputs/2.txt", "r")
    lines = [[int(char) for char in line.strip().split(" ")] for line in file]
    safeCount = 0
    for line in lines:
        if sortedAndDifference(line):
            safeCount += 1
            continue
        for i in range(len(line)):
            newLine = line[:i] + line[i + 1:]
            if sortedAndDifference(newLine):
                safeCount += 1
                break
    print(safeCount)


if __name__ == '__main__':
    main()