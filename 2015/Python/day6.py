def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/6.txt", "r")
    lights = [[0] * 1000 for _ in range(1000)]
    for line in file:
        line = line.strip()
        toggle = False
        turnOn = False
        firstNum = 0
        if line.startswith("toggle"):
            toggle = True
            firstNum = 7
        elif line.startswith("turn"):
            if line[5:7].strip() == "on":
                turnOn = True
                firstNum = 8
            else:
                firstNum = 9
        secondNum = line.find("through") + 8

        start = (int(line[firstNum : line.find(",")]), int(line[line.find(",") + 1 : line.find("through") - 1]))
        secondComma = line[line.find(",") + 1 :].find(",") + line.find(",") + 1
        end = (int(line[secondNum : secondComma]), int(line[secondComma + 1 :]))

        for r in range(start[1], end[1] + 1):
            for c in range(start[0], end[0] + 1):
                if toggle:
                    lights[r][c] = 1 - lights[r][c]
                elif turnOn:
                    lights[r][c] = 1
                else:
                    lights[r][c] = 0

    count = 0
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            if lights[i][j] == 1:
                count += 1
    print(count)

def partTwo():
    file = open("Inputs/6.txt", "r")
    lights = [[0] * 1000 for _ in range(1000)]
    for line in file:
        line = line.strip()
        toggle = False
        turnOn = False
        firstNum = 0
        if line.startswith("toggle"):
            toggle = True
            firstNum = 7
        elif line.startswith("turn"):
            if line[5:7].strip() == "on":
                turnOn = True
                firstNum = 8
            else:
                firstNum = 9
        secondNum = line.find("through") + 8

        start = (int(line[firstNum: line.find(",")]), int(line[line.find(",") + 1: line.find("through") - 1]))
        secondComma = line[line.find(",") + 1:].find(",") + line.find(",") + 1
        end = (int(line[secondNum: secondComma]), int(line[secondComma + 1:]))

        for r in range(start[1], end[1] + 1):
            for c in range(start[0], end[0] + 1):
                if toggle:
                    lights[r][c] += 2
                elif turnOn:
                    lights[r][c] += 1
                else:
                    lights[r][c] -= 1
                    if lights[r][c] < 0:
                        lights[r][c] = 0

    brightness = 0
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            brightness += lights[i][j]
    print(brightness)


if __name__ == '__main__':
    main()