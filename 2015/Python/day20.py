import math


def main():
    partOne()
    partTwo()


def getGoal():
    file = open("Inputs/20.txt", "r")
    return [int(line.strip()) for line in file][0]


def sumFactors(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return sum(factors)


def partOne():
    goal = getGoal()
    i = 1
    while True:
        numPresents = sumFactors(i) * 10
        if numPresents >= goal:
            print(i)
            break
        i += 1


def partTwo():
    goal = getGoal()
    houses = [0] * 1000000
    for elf in range(1, len(houses)):
        count = 0
        for house in range(elf, len(houses), elf):
            houses[house] += elf * 11
            count += 1
            if count == 50:
                break
    for house_number, presents in enumerate(houses):
        if presents >= goal:
            print(house_number)
            break


if __name__ == '__main__':
    main()