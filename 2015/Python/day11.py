def main():
    print(''.join(partOne()))
    partTwo()


def increment(line):
    hasThreeIncreasing = False
    hasDisallowed = any(x in ['i', 'o', 'l'] for x in line)
    hasTwoPairs = False
    while not (hasThreeIncreasing and not hasDisallowed and hasTwoPairs):
        for i in range(len(line) - 1, -1, -1):
            if line[i] == 'z':
                line[i] = 'a'
                if i == 0:
                    line.insert(0, 'a')
            else:
                line[i] = chr(ord(line[i]) + 1)
                break

        hasThreeIncreasing = any(
            ord(line[i]) == ord(line[i + 1]) - 1 == ord(line[i + 2]) - 2
            for i in range(len(line) - 2)
        )

        hasDisallowed = any(x in ['i', 'o', 'l'] for x in line)

        pairs = set()
        i = 0
        while i < len(line) - 1:
            if line[i] == line[i + 1]:
                pairs.add(line[i])
                i += 1
            i += 1
        hasTwoPairs = len(pairs) >= 2
    return line


def partOne():
    file = open("Inputs/11.txt", "r")
    line = [[char for char in line.strip()] for line in file][0]
    return increment(line)


def partTwo():
    line = increment(partOne())
    print(''.join(line))


if __name__ == '__main__':
    main()