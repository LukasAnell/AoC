import json


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/12.txt", "r")
    line = [[char for char in line] for line in file][0]

    sumNums = 0
    num = ''
    for char in line:
        if char.isdigit() or (char == '-' and num == ''):
            num += char
        else:
            if num:
                sumNums += int(num)
                num = ''
    if num:
        sumNums += int(num)
    print(sumNums)


def partTwo():
    file = open("Inputs/12.txt", "r")
    data = json.load(file)

    def sumNums(obj):
        if isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            return sum(sumNums(v) for v in obj.values())
        elif isinstance(obj, list):
            return sum(sumNums(i) for i in obj)
        elif isinstance(obj, int):
            return obj
        return 0

    totalSum = sumNums(data)
    print(totalSum)


if __name__ == '__main__':
    main()