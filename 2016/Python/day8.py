from collections import deque


def main():
    partOne()
    partTwo()


def createRect(screen, width, height):
    screenCopy = screen.copy()
    for i in range(height):
        for j in range(width):
            screenCopy[i][j] = '#'
    return screenCopy


def rotateRow(screen, rowNum, amount):
    screenCopy = screen.copy()
    row = deque(screen[rowNum])
    row.rotate(amount)
    screenCopy[rowNum] = list(row)
    return screenCopy


def rotateColumn(screen, colNum, amount):
    screenCopy = screen.copy()
    numRows = len(screenCopy)
    amount %= numRows
    col = [screenCopy[rowNum][colNum] for rowNum in range(numRows)]
    rotatedCol = col[-amount:] + col[:-amount]
    for rowNum in range(numRows):
        row = list(screenCopy[rowNum])
        row[colNum] = rotatedCol[rowNum]
        screenCopy[rowNum] = row
    return screenCopy


def getScreenAfterTransform():
    file = open("Inputs/8.txt", "r")
    screen = [['.' for _ in range(50)] for _ in range(6)]
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "rect":
            width, height = [int(num) for num in line[1].split("x")]
            screen = createRect(screen, width, height)
        elif line[0] == "rotate":
            if line[1] == "row":
                rowNum = int(line[2].split("=")[1])
                amount = int(line[4])
                screen = rotateRow(screen, rowNum, amount)
            elif line[1] == "column":
                colNum = int(line[2].split("=")[1])
                amount = int(line[4])
                screen = rotateColumn(screen, colNum, amount)
    return screen


def partOne():
    screen = getScreenAfterTransform()
    print(''.join(''.join(char for char in row) for row in screen).count('#'))


def partTwo():
    screen = getScreenAfterTransform()
    for i in range(len(screen)):
        print(''.join(char if char == '#' else " " for char in screen[i]))


if __name__ == '__main__':
    main()