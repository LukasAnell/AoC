def main():
    partOne()
    partTwo()


def partOne():
    line = [[int(digit) for digit in line.strip()] for line in open("Inputs/1.txt", "r")][0]
    sumDigits = 0
    for i in range(len(line) - 1):
        currentDigit, nextDigit = line[i], line[i + 1]
        if currentDigit == nextDigit:
            sumDigits += currentDigit
    if line[0] == line[-1]:
        sumDigits += line[0]
    print(sumDigits)


def partTwo():
    line = [[int(digit) for digit in line.strip()] for line in open("Inputs/1.txt", "r")][0]
    sumDigits = 0
    for i in range(len(line)):
        currentDigit, aroundDigit = line[i], line[(i + len(line) // 2) % len(line)]
        if currentDigit == aroundDigit:
            sumDigits += currentDigit
    print(sumDigits)


if __name__ == '__main__':
    main()
