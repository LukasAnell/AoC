def main():
    partOne()
    partTwo()


def getInitialState():
    file = open("Inputs/16.txt", "r")
    return [line.strip() for line in file][0]


def calculateChecksum(state, goalLength):
    while len(state) < goalLength:
        state = state + '0' + ''.join(['1' if c == '0' else '0' for c in state[::-1]])
    checksum = state[:goalLength]
    while len(checksum) % 2 == 0:
        checksum = ''.join(['1' if checksum[i] == checksum[i+1] else '0' for i in range(0, len(checksum), 2)])
    return checksum


def partOne():
    goalLength = 272
    print(calculateChecksum(getInitialState(), goalLength))


def partTwo():
    goalLength = 35651584
    print(calculateChecksum(getInitialState(), goalLength))


if __name__ == '__main__':
    main()
