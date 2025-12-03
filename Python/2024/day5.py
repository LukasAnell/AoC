def main():
    partOne()
    partTwo()


def getRulesAndUpdates():
    file = open("Inputs/5.txt", "r")
    rules = []
    updates = []
    for line in file:
        line = line.strip()
        if '|' in line:
            rules += [[int(num) for num in line.split("|")]]
        elif ',' in line:
            updates += [[int(num) for num in line.split(",")]]
    return rules, updates


def isUpdateValid(line, rules):
    for i in range(len(line)):
        for rule in rules:
            if line[i] == rule[1]:
                for j in range(i, len(line)):
                    if line[j] == rule[0]:
                        return False
    return True



def partOne():
    rules, updates = getRulesAndUpdates()
    total = 0
    for line in updates:
        if isUpdateValid(line, rules):
            total += line[len(line) // 2]
    print(total)


def ruleSort(line, rules) -> list():
    lineCopy = line[:]
    while not isUpdateValid(lineCopy, rules):
        for i in range(len(lineCopy)):
            for rule in rules:
                if lineCopy[i] == rule[1]:
                    for j in range(i, len(lineCopy)):
                        if lineCopy[j] == rule[0]:
                            lineCopy[i], lineCopy[j] = lineCopy[j], lineCopy[i]
    return lineCopy


def partTwo():
    rules, updates = getRulesAndUpdates()
    total = 0
    for line in updates:
        if not isUpdateValid(line, rules):
            total += ruleSort(line, rules)[len(line) // 2]
    print(total)


if __name__ == '__main__':
    main()