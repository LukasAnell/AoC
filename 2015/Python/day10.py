def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/10.txt", "r")
    line = [int(char) for char in file.readline().strip()]
    print(line)
    compressedLine = []
    i = 0
    while i < len(line):
        count = 1
        while i + 1 < len(line) and line[i] == line[i + 1]:
            count += 1
            i += 1
        compressedLine.append({line[i]: count})
        i += 1
    print(compressedLine)



def partTwo():
    pass


if __name__ == '__main__':
    main()