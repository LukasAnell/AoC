def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/1.txt", "r")
    print(sum(int(row[0] + row[-1]) for row in [[char for char in line.strip() if char.isdigit()] for line in file]))


def partTwo():
    wordToNum = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    file = open("Inputs/1.txt", "r")
    lines = []
    for line in file:
        lineCopy = line.strip()
        for word in wordToNum:
            if word in lineCopy:
                lineCopy = lineCopy.replace(word, word[:len(word) // 2] + str(wordToNum[word]) + word[len(word) // 2:])
        lines.append(lineCopy)
    print(sum(int(row[0] + row[-1]) for row in [[char for char in line.strip() if char.isdigit()] for line in lines]))


if __name__ == '__main__':
    main()
