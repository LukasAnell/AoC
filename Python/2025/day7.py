from Python.Utilities.utils import readInputLines

lines = readInputLines()


def main():
    partOne()
    partTwo()


def partOne():
    grid = [list(line.strip()) for line in lines]

    startCol = -1
    startRow = -1
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                startCol = c
                startRow = r
                break
        if startCol != -1:
            break

    activeBeams = {startCol}
    splitCount = 0
    for r in range(startRow + 1, len(grid)):
        newBeams = set()
        for beamCol in activeBeams:
            if 0 <= beamCol < len(grid[r]):
                cell = grid[r][beamCol]
                if cell == "^":
                    splitCount += 1
                    if beamCol - 1 >= 0:
                        newBeams.add(beamCol - 1)

                    if beamCol + 1 < len(grid[r]):
                        newBeams.add(beamCol + 1)
                elif cell == "." or cell == " ":
                    newBeams.add(beamCol)

        activeBeams = newBeams
        if not activeBeams:
            break

    print(splitCount)


def partTwo():
    pass


if __name__ == "__main__":
    main()
