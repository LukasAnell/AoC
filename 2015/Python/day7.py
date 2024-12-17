def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/7.txt", "r")
    wireMap = {}
    for line in file:
        pass


    for line in file:
        line = line.strip()
        splitLine = line.split(" ")
        if splitLine[1] == "->":
            if splitLine[0].isdigit(): source = int(splitLine[0])
            else: source = wireMap.get(splitLine[0])
            destination = splitLine[2]
            wireMap[destination] = source
        elif splitLine[2] == "->":
            destination = splitLine[3]
            source = splitLine[1]
            if wireMap.get(source) is None:
                wireMap[source] = 0
            source = int(wireMap.get(source))
            wireMap[destination] = source ^ 0b1111111111111111
        elif splitLine[3] == "->":
            op = splitLine[1]
            destination = splitLine[4]
            first = splitLine[0]
            second = splitLine[2]
            if wireMap.get(first) is None:
                wireMap[first] = 0
            if wireMap.get(second) is None and not second.isdigit():
                wireMap[second] = 0
            if op == "AND":
                wireMap[destination] = wireMap.get(first) & wireMap.get(second)
            if op == "OR":
                wireMap[destination] = wireMap.get(first) | wireMap.get(second)
            if op == "LSHIFT":
                wireMap[destination] = wireMap.get(first) << int(second)
            if op == "RSHIFT":
                wireMap[destination] = wireMap.get(first) >> int(second)
    print(sum([int(value) for value in wireMap.values()]))

def partTwo():
    pass

if __name__ == '__main__':
    main()