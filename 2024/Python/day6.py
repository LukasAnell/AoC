from functools import cache


def main():
    partOne()
    partTwo()


def getLinesObstaclesStart():
    file = open("Inputs/6.txt", "r")
    lines = [line.strip() for line in file]
    startingPosition = ()
    obstacles = set()
    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            char = line[j]
            if char == '^':
                startingPosition = (i, j)
            if char == '#':
                obstacles.add((i, j))
    return lines, obstacles, startingPosition


def withinBounds(currentPosition, lines):
    y, x = currentPosition
    if y >= len(lines) or y < 0:
        return False
    if x >= len(lines[0]) or x < 0:
        return False
    return True


def getVisited(lines, obstacles, startingPosition):
    currentPosition = startingPosition
    visited = set()
    direction = 0
    while withinBounds(currentPosition, lines):
        y, x = currentPosition
        visited.add(currentPosition)
        if direction == 0:
            newPosition = (y - 1, x)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 1:
            newPosition = (y, x + 1)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 2:
            newPosition = (y + 1, x)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 3:
            newPosition = (y, x - 1)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
    return visited


def partOne():
    lines, obstacles, startingPosition = getLinesObstaclesStart()
    print(len(getVisited(lines, obstacles, startingPosition)))


def checkLoop(lines, obstacles, startingPosition):
    currentPosition = startingPosition
    visited = set()
    direction = 0
    i = 0
    while withinBounds(currentPosition, lines) and i < 10_000:
        y, x = currentPosition
        visited.add(currentPosition)
        if direction == 0:
            newPosition = (y - 1, x)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 1:
            newPosition = (y, x + 1)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 2:
            newPosition = (y + 1, x)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        if direction == 3:
            newPosition = (y, x - 1)
            if newPosition in obstacles:
                direction = (direction + 1) % 4
            else:
                currentPosition = newPosition
        i += 1
    return i >= 9999


def partTwo():
    lines, obstacles, startingPosition = getLinesObstaclesStart()
    visited = getVisited(lines, obstacles, startingPosition)
    visited.remove(startingPosition)
    count = 0
    for (y, x) in visited:
        newObstacles = set(list(obstacles) + [(y, x)])
        if checkLoop(lines, newObstacles, startingPosition):
            count += 1
    print(count)


if __name__ == '__main__':
    main()