def main():
    partOne()
    partTwo()


def findLinesByCol():
    file = open("Inputs/6.txt", "r")
    return list(map(list, zip(*[line.strip() for line in file])))


def findMostCommon(chars):
    charCount = {}
    for char in chars:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1
    return max(charCount, key=charCount.get)


def partOne():
    linesByCol = findLinesByCol()
    message = ""
    for col in linesByCol:
        message += findMostCommon(col)
    print(message)


def findLeastCommon(chars):
    charCount = {}
    for char in chars:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1
    return min(charCount, key=charCount.get)


def partTwo():
    linesByCol = findLinesByCol()
    message = ""
    for col in linesByCol:
        message += findLeastCommon(col)
    print(message)


if __name__ == '__main__':
    main()