def main():
    partOne(100)
    partTwo(100)


def iterateLights(lightsGrid):
    newGrid = [['.' for _ in range(len(lightsGrid[0]))] for _ in range(len(lightsGrid))]
    for r in range(len(lightsGrid)):
        for c in range(len(lightsGrid[0])):
            onNeighbors = countOnNeighbors(lightsGrid, r, c)
            if lightsGrid[r][c] == '#' and onNeighbors in [2, 3]:
                newGrid[r][c] = '#'
            elif lightsGrid[r][c] == '.' and onNeighbors == 3:
                newGrid[r][c] = '#'
            else:
                newGrid[r][c] = '.'
    return newGrid


def countOnNeighbors(grid, y, x):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '#':
            count += 1
    return count


def partOne(steps):
    file = open("Inputs/18.txt", "r")
    lightsGrid = [[char for char in line.strip()] for line in file]
    for _ in range(steps):
        lightsGrid = iterateLights(lightsGrid)
    lightsCount = 0
    for row in lightsGrid:
        lightsCount += ''.join(row).count('#')
    print(lightsCount)


def turnOnCorners(grid):
    grid[0][0] = '#'
    grid[0][len(grid[0]) - 1] = '#'
    grid[len(grid) - 1][0] = '#'
    grid[len(grid) - 1][len(grid[0]) - 1] = '#'


def partTwo(steps):
    file = open("Inputs/18.txt", "r")
    lightsGrid = [[char for char in line.strip()] for line in file]
    turnOnCorners(lightsGrid)
    for _ in range(steps):
        lightsGrid = iterateLights(lightsGrid)
        turnOnCorners(lightsGrid)
    lightsCount = 0
    for row in lightsGrid:
        lightsCount += ''.join(row).count('#')
    print(lightsCount)


if __name__ == '__main__':
    main()