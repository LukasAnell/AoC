def main():
    partOne()
    partTwo()


def getTiles():
    file = open("Inputs/18.txt", "r")
    return [line.strip() for line in file][0]


def getRows(rows, rowCount):
    for _ in range(rowCount - 1):
        prevRow = rows[-1]
        newRow = ""
        for i in range(len(prevRow)):
            left = prevRow[i - 1] if i > 0 else "."
            center = prevRow[i]
            right = prevRow[i + 1] if i < len(prevRow) - 1 else "."
            if (left == "^" and center == "^" and right == ".") or \
                    (left == "." and center == "^" and right == "^") or \
                    (left == "^" and center == "." and right == ".") or \
                    (left == "." and center == "." and right == "^"):
                newRow += "^"
            else:
                newRow += "."
        rows.append(newRow)
    return rows


def partOne():
    rowCount = 40
    print(sum(row.count(".") for row in getRows([getTiles()], rowCount)))


def partTwo():
    rowCount = 400000
    print(sum(row.count(".") for row in getRows([getTiles()], rowCount)))


if __name__ == "__main__":
    main()
