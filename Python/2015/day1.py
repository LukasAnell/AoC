def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/1.txt", "r")
    print(sum(line.count("(") - line.count(")") for line in file))

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