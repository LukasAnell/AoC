from Python.Utilities.utils import readInputLines

lines = readInputLines()


def main():
    partOne()
    partTwo()


def partOne():
    output = 0
    for line in lines:
        line = line.strip()

        largest = findLargestDigit(line)
        if line.index(str(largest)) == len(line) - 1:
            largest = findLargestDigit(line[:line.index(str(largest))])

        line = line[line.index(str(largest)) + 1:]
        secondLargest = findLargestDigit(line)

        output += int(str(largest) + str(secondLargest))

    print(output)


def findLargestDigit(line):
    largest = -1
    for char in line:
        if char.isdigit():
            digit = int(char)
            if digit > largest:
                largest = digit
    return largest


def partTwo():
    output = 0
    for line in lines:
        line = line.strip()

        current = ""
        position = 0
        amountLeft = 12
        while amountLeft > 0:
            largest = -1
            bestIndex = position
            for i in range(position, len(line) - amountLeft + 1):
                digit = int(line[i])

                if digit > largest:
                    largest = digit
                    bestIndex = i

                    if largest == 9:
                        break

            current += str(largest)
            position = bestIndex + 1
            amountLeft -= 1

        output += int(current)

    print(output)


if __name__ == '__main__':
    main()
