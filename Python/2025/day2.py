from Python.Utilities.utils import readInputLines

lines = readInputLines()


def main():
    partOne()
    partTwo()


def partOne():
    ranges = []
    for line in lines:
        ranges += line.strip().split(",")
    total = 0
    for r in ranges:
        if "-" not in r:
            continue

        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])

        for i in range(lower, upper + 1):
            if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
                total += i
    print(total)


def partTwo():
    ranges = []
    for line in lines:
        ranges += line.strip().split(",")
    total = 0
    for r in ranges:
        if "-" not in r:
            continue

        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])

        for i in range(lower, upper + 1):
            if isRepetition(str(i)):
                total += i

    print(total)


def isRepetition(inputString: str):
    length = len(inputString)

    for l in range(1, length // 2 + 1):
        if length % l != 0:
            continue

        if inputString == inputString[:l] * (length // l):
            return True

    return False


if __name__ == '__main__':
    main()
