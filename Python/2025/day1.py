def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/1.txt", "r")
    times = 0
    currentNum = 50
    for line in file:
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            currentNum = (currentNum + distance) % 100
        else:
            currentNum = (currentNum - distance) % 100

        if currentNum == 0:
            times += 1

    print(times)


def partTwo():
    file = open("Inputs/1.txt", "r")
    times = 0
    currentNum = 50
    for line in file:
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            if currentNum != 0:
                distanceToZero = 100 - currentNum
            else:
                distanceToZero = 100

            if distance >= distanceToZero:
                times += 1 + (distance - distanceToZero) // 100

            currentNum = (currentNum + distance) % 100
        else:
            if currentNum != 0:
                distanceToZero = currentNum
            else:
                distanceToZero = 100

            if distance >= distanceToZero:
                times += 1 + (distance - distanceToZero) // 100

            currentNum = (currentNum - distance) % 100

    print(times)


if __name__ == '__main__':
    main()