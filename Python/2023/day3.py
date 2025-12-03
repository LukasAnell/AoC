def main():
    partOne()
    partTwo()


def checkAround(schematic, r, c):
    rows = len(schematic)
    cols = len(schematic[0])
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if schematic[i][j] in '*#$.+':
                return True
    return False


def reconstructNum(line, c):
    num = 0
    for i in range(c - 1, c + 2):
        num = num * 10 + int(line[i])
    return num


def partOne():
    file = open("Inputs/3.txt", "r")
    schematic = [[char for char in line.strip()] for line in file]
    enginePartSum = 0
    rows = len(schematic)
    cols = len(schematic[0])
    for r, line in enumerate(schematic):
        for c, char in enumerate(line):
            if char.isdigit():
                pass
    print(enginePartSum)


def partTwo():
    pass


if __name__ == '__main__':
    main()