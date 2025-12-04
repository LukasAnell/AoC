from Python.Utilities.utils import readInputLines


def main():
    partOne()
    partTwo()


def partOne():
    grid = [[c for c in line.strip()] for line in readInputLines()]

    rolls = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == ".":
                continue

            count = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue

                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[r]) and grid[r + dr][c + dc] == "@":
                        count += 1

            if count < 4:
                rolls += 1

    print(rolls)


def partTwo():
    grid = [[c for c in line.strip()] for line in readInputLines()]

    rolls = 0
    rollsLeft = True
    while rollsLeft:
        oldRollsCount = rolls
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == ".":
                    continue

                count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue

                        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[r]) and grid[r + dr][c + dc] == "@":
                            count += 1

                if count < 4:
                    grid[r][c] = "."
                    rolls += 1

        if oldRollsCount == rolls:
            rollsLeft = False

    print(rolls)


if __name__ == '__main__':
    main()
