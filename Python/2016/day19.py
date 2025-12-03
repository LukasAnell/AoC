def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/19.txt", "r")
    numElves = int([line.strip() for line in file][0])
    elves = [(i, 1) for i in range(1, numElves + 1)]
    while len(elves) > 1:
        for i in range(len(elves)):
           pass


def partTwo():
    pass


if __name__ == "__main__":
    main()
