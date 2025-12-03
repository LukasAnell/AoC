def main():
    partOne()
    partTwo()


def evaluateExpression(equation, operators, target):
    result = ""
    for i in range(len(operators)):
        if operators[i] == '||':
            result += str(equation[i])
        else:
            result += str(equation[i]) + operators[i]
    result += str(equation[-1])
    output = int(eval(result)) == target
    return output


def generateOperators(operators, index, equation, target, isPartOne):
    if index == len(operators):
        if evaluateExpression(equation, operators, target):
            found = True
        return
    operators[index] = '+'
    generateOperators(operators, index + 1, equation, target, isPartOne)
    operators[index] = '*'
    generateOperators(operators, index + 1, equation, target, isPartOne)
    if not isPartOne:
        operators[index] = '||'
        generateOperators(operators, index + 1, equation, target, isPartOne)


def partOne():
    file = open("Inputs/7.txt", "r")
    calibrationResult = 0
    for line in file:
        line = line.strip()
        target = int(line.split(": ")[0])
        equation = [int(num) for num in line.split(": ")[1].split(" ")]
        operators = ['' for _ in range(len(equation) - 1)]
        generateOperators(operators, 0, equation, target, True)
        if found:
            calibrationResult += target
    print(calibrationResult)


def partTwo():
    pass


if __name__ == '__main__':
    main()