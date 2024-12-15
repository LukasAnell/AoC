def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/1.txt", "r")
    floor = 0
    for line in file:
        for char in line:
            if char == "(":
                floor += 1
            else:
                floor -= 1
    print(floor, end="\n")

def partTwo():
    file = open("Inputs/1.txt", "r")
    floor = 0
    for line in file:
        for i in range(len(line)):
            if floor == -1:
                print(i)
                return
            if line[i] == "(":
                floor += 1
            else:
                floor -= 1

if __name__ == '__main__':
    main()