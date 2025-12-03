def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/8.txt", "r")
    codeCount = 0
    memoryCount = 0
    for line in file:
        line = line.strip()
        codeCount += len(line)
        memoryCount += len(eval(line))
    print(codeCount - memoryCount)


def partTwo():
    file = open("Inputs/8.txt", "r")
    originalCount = 0
    encodedCount = 0
    for line in file:
        line = line.strip()
        originalCount += len(line)
        encodedLine = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        encodedCount += len(encodedLine)
    print(encodedCount - originalCount)


if __name__ == '__main__':
    main()