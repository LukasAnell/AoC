def main():
    partOne()
    partTwo()


def getDiscs():
    file = open("Inputs/15.txt", "r")
    discs = []
    for line in file:
        line = line.strip().split(" ")
        discs.append([int(line[3]), int(line[-1][:-1])])
    return discs


def findFirstTime(discs):
    time = 0
    while True:
        success = True
        for i in range(len(discs)):
            if (discs[i][1] + time + i + 1) % discs[i][0] != 0:
                success = False
                break
        if success:
            break
        time += 1
    return time


def partOne():
    print(findFirstTime(getDiscs()))


def partTwo():
    discs = getDiscs()
    discs.append([11, 0])
    print(findFirstTime(discs))


if __name__ == "__main__":
    main()