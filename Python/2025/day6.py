import re

from Python.Utilities.utils import readInputLines

lines = readInputLines()


def main():
    partOne()
    partTwo()


def partOne():
    operatorsList = []
    runningTotals = [0]
    for line in lines[::-1]:
        line = line.strip()
        if not line:
            continue

        if "+" in line or "*" in line:
            operatorsList = re.split("\\s+", line.strip())
            runningTotals = [0 for _ in range(len(re.split("\\s+", line)))]
        else:
            if runningTotals[0] == 0:
                runningTotals = [int(num) for num in re.split("\\s+", line)]
                continue

            currentLine = [int(num) for num in re.split("\\s+", line)]
            for i in range(0, len(currentLine)):
                if operatorsList[i] == "+":
                    runningTotals[i] = runningTotals[i] + currentLine[i]
                elif operatorsList[i] == "*":
                    runningTotals[i] = runningTotals[i] * currentLine[i]

    print(sum(runningTotals))


def partTwo():
    charGrid = []
    operatorLine = ""

    for line in lines:
        line = line.rstrip('\n')
        if not line.strip():
            continue

        if "+" in line or "*" in line:
            operatorLine = line.strip()
        else:
            charGrid.append(list(line))

    maxLen = max(len(line) for line in charGrid + [operatorLine])
    charGrid = ["".join(line).ljust(maxLen) for line in charGrid]
    operatorLine = operatorLine.ljust(maxLen)

    columns = list(zip(*charGrid))

    problems = []
    currentProblem = []
    currentOperator = None

    for i, col in enumerate(columns):
        if all(c == ' ' for c in col):
            if currentProblem:
                problems.append((currentProblem, currentOperator))
                currentProblem = []
                currentOperator = None
        else:
            numbers = []
            currentNum = ""
            for c in col:
                if c.isdigit():
                    currentNum += c
                else:
                    if currentNum:
                        numbers.append(int(currentNum))
                        currentNum = ""
            if currentNum:
                numbers.append(int(currentNum))

            currentProblem.append(numbers)
            if i < len(operatorLine) and operatorLine[i] in "+*":
                currentOperator = operatorLine[i]

    if currentProblem:
        problems.append((currentProblem, currentOperator))

    total = 0
    for cols, operator in reversed(problems):
        result = 0
        allNums = [n for col in cols for n in col]
        if operator == "+":
            result = sum(allNums)
        elif operator == "*":
            result = 1
            for n in allNums:
                result *= n
        total += result

    print(total)


if __name__ == "__main__":
    main()
