def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/2.txt", "r")
    checksum = 0
    for line in file:
        line = [int(number) for number in line.strip().split()]
        difference = max(line) - min(line)
        checksum += difference
    print(checksum)


def partTwo():
    file = open("Inputs/2.txt", "r")
    checksum = 0
    for line in file:
        line = [int(number) for number in line.strip().split()]
        found = False
        for i in range(len(line)):
            for j in range(len(line)):
                if i == j:
                    continue
                if line[i] % line[j] == 0:
                    checksum += line[i] // line[j]
                    found = True
                    break
            if found:
                break
    print(checksum)


if __name__ == '__main__':
    main()
