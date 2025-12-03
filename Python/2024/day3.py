import re


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/3.txt", "r")
    lines = [line.strip() for line in file]
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for line in lines:
        matches = pattern.findall(line)
        total += sum([int(match[0]) * int(match[1]) for match in matches])
    print(total)


def partTwo():
    file = open("Inputs/3.txt", "r")
    lines = [line.strip() for line in file]
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    total = 0
    skip = False
    for line in lines:
        matches = pattern.findall(line)
        for match in matches:
            if "don't()" in match:
                skip = True
            if "do()" in match:
                skip = False
            if "mul" in match and not skip:
                nums = match[4:-1].split(",")
                total += int(nums[0]) * int(nums[1])
    print(total)


if __name__ == '__main__':
    main()