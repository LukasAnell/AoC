def main():
    partOne()
    partTwo()

def getValue(wire, wireVals, wireMap):
    if wire.isdigit():
        return int(wire)
    if wire not in wireVals:
        expr = wireMap[wire]
        if len(expr) == 1:
            wireVals[wire] = getValue(expr[0], wireVals, wireMap)
        elif len(expr) == 2:
            wireVals[wire] = ~getValue(expr[1], wireVals, wireMap) & 0xFFFF
        elif len(expr) == 3:
            op1, op, op2 = expr
            if op == "AND":
                wireVals[wire] = getValue(op1, wireVals, wireMap) & getValue(op2, wireVals, wireMap)
            elif op == "OR":
                wireVals[wire] = getValue(op1, wireVals, wireMap) | getValue(op2, wireVals, wireMap)
            elif op == "LSHIFT":
                wireVals[wire] = getValue(op1, wireVals, wireMap) << getValue(op2, wireVals, wireMap)
            elif op == "RSHIFT":
                wireVals[wire] = getValue(op1, wireVals, wireMap) >> getValue(op2, wireVals, wireMap)
    return wireVals[wire]

def partOne():
    file = open("Inputs/7.txt", "r")
    wireMap = {}
    wireVals = {}
    for line in file:
        line = line.strip()
        splitLine = [sect.strip() for sect in line.split("->")]
        wireMap[splitLine[1]] = splitLine[0].split(" ")

    result = getValue('a', wireVals, wireMap)
    print(result)


def partTwo():
    file = open("Inputs/7.txt", "r")
    wireMap = {}
    wireVals = {}
    for line in file:
        line = line.strip()
        splitLine = [sect.strip() for sect in line.split("->")]
        wireMap[splitLine[1]] = splitLine[0].split(" ")
    signal_a = getValue('a', wireVals, wireMap)
    wireMap['b'] = [str(signal_a)]
    wireVals = {}
    result = getValue('a', wireVals, wireMap)
    print(result)


if __name__ == '__main__':
    main()