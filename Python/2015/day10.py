def main():
    partOne()
    partTwo()


def lookAndSay(sequence):
    result = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + sequence[i])
        i += 1
    return ''.join(result)


def partOne():
    file = open("Inputs/10.txt", "r")
    line = [char for char in file.readline().strip()]
    for _ in range(40):
        line = lookAndSay(line)

    print(len(line))


def partTwo():
    file = open("Inputs/10.txt", "r")
    line = [char for char in file.readline().strip()]
    for _ in range(50):
        line = lookAndSay(line)

    print(len(line))


if __name__ == '__main__':
    main()