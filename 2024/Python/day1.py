import functools


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/1.txt", "r")
    left, right = (sorted(list(x)) for x in zip(*[(int(pair[0]), int(pair[1])) for pair in [line.strip().split("   ") for line in file]]))
    print(sum(abs(x - y) for x, y in zip(left, right)))


@functools.cache
def partTwo():
    file = open("Inputs/1.txt", "r")
    left, right = (list(x) for x in zip(*[(int(pair[0]), int(pair[1])) for pair in [line.strip().split("   ") for line in file]]))
    print(sum(num * right.count(num) for num in left))


if __name__ == '__main__':
    main()