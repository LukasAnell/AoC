from Python.Utilities.utils import readInputLines


def main():
    partOne()
    partTwo()


def partOne():
    lines = readInputLines()

    freshCount = 0
    rangesList = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "-" in line:
            rangesList += [[int(num) for num in line.split("-")]]
        else:
            for r in rangesList:
                if r[0] <= int(line) <= r[1]:
                    freshCount += 1
                    break

    print(freshCount)


def partTwo():
    lines = readInputLines()

    rangesList = []
    for line in lines:
        line = line.strip()
        if not line or '-' not in line:
            continue

        currentRange = [int(num) for num in line.split("-")]
        addOrMergeRange(rangesList, currentRange)

    freshCount = 0
    for r in rangesList:
        freshCount += r[1] - r[0] + 1

    print(freshCount)


def addOrMergeRange(rangesList, newRange):
    start, end = sorted(newRange)
    combinedRanges = sorted(rangesList + [[start, end]], key=lambda element: element[0])

    mergedRanges = []
    for r in combinedRanges:
        if not mergedRanges:
            mergedRanges.append(r.copy())
            continue

        lastRange = mergedRanges[-1]
        if r[0] <= lastRange[1] + 1:
            lastRange[1] = max(lastRange[1], r[1])
        else:
            mergedRanges.append(r.copy())

    rangesList[:] = mergedRanges
    return rangesList


if __name__ == '__main__':
    main()
