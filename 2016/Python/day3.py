def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/3.txt", "r")
    lines = [sorted([int(char.strip()) for char in line.strip().split(" ") if char.strip()]) for line in file]
    count = 0
    for line in lines:
        if line[0] + line[1] > line[2]:
            count += 1
    print(count)


def partTwo():
    file = open("Inputs/3.txt", "r")
    lines = [[int(char.strip()) for char in line.strip().split(" ") if char.strip()] for line in file]
    count = 0
    for i in range(0, len(lines), 3):
        for j in range(3):
            line = sorted([lines[i][j], lines[i + 1][j], lines[i + 2][j]])
            if line[0] + line[1] > line[2]:
                count += 1
    print(count)


if __name__ == '__main__':
    main()