import itertools


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/17.txt", "r")
    containers = [int(line.strip()) for line in file]
    target = 150
    count = 0
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == target:
                count += 1
    print(count)


def partTwo():
    file = open("Inputs/17.txt", "r")
    containers = [int(line.strip()) for line in file]
    target = 150
    validCombinations = []
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == target:
                validCombinations.append(combination)
    minContainers = min(len(combination) for combination in validCombinations)
    minCombinationsCount = sum(1 for combination in validCombinations if len(combination) == minContainers)
    print(minCombinationsCount)


if __name__ == '__main__':
    main()