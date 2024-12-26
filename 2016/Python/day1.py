def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/1.txt", "r")
    lines = [line.strip() for line in file][0].split(", ")
    print(lines)


def partTwo():
    pass


if __name__ == '__main__':
    main()