def main():
    partOne()
    partTwo()

def getFavNumAndMaze():
    file = open("Inputs/13.txt", "r")
    favoriteNumber = int([line.strip() for line in file][0])
    maze = []
    for y in range(50):
        row = []
        for x in range(50):
            value = x * x + 3 * x + 2 * x * y + y + y * y + favoriteNumber
            binary = bin(value)[2:]
            if binary.count("1") % 2 == 0:
                row.append(".")
            else:
                row.append("#")
        maze.append(row)
    return favoriteNumber, maze


def partOne():
    favoriteNumber, maze = getFavNumAndMaze()
    startingPoint = (1, 1)
    endPoint = (31, 39)
    steps = 0
    visited = []
    queue = [(startingPoint, steps)]
    while queue:
        currentPoint, steps = queue.pop(0)
        if currentPoint == endPoint:
            print(steps)
            break
        visited.append(currentPoint)
        x, y = currentPoint
        if x > 0 and maze[y][x - 1] == "." and (x - 1, y) not in visited:
            queue.append(((x - 1, y), steps + 1))
        if y > 0 and maze[y - 1][x] == "." and (x, y - 1) not in visited:
            queue.append(((x, y - 1), steps + 1))
        if x < 49 and maze[y][x + 1] == "." and (x + 1, y) not in visited:
            queue.append(((x + 1, y), steps + 1))
        if y < 49 and maze[y + 1][x] == "." and (x, y + 1) not in visited:
            queue.append(((x, y + 1), steps + 1))


def partTwo():
    favoriteNumber, maze = getFavNumAndMaze()
    startingPoint = (1, 1)
    steps = 0
    visited = set()
    queue = [(startingPoint, steps)]
    while queue:
        currentPoint, steps = queue.pop(0)
        if steps <= 50:
            visited.add(currentPoint)
        else:
            break
        x, y = currentPoint
        if x > 0 and maze[y][x - 1] == "." and (x - 1, y) not in visited:
            queue.append(((x - 1, y), steps + 1))
        if y > 0 and maze[y - 1][x] == "." and (x, y - 1) not in visited:
            queue.append(((x, y - 1), steps + 1))
        if x < 49 and maze[y][x + 1] == "." and (x + 1, y) not in visited:
            queue.append(((x + 1, y), steps + 1))
        if y < 49 and maze[y + 1][x] == "." and (x, y + 1) not in visited:
            queue.append(((x, y + 1), steps + 1))
    print(len(visited))


if __name__ == "__main__":
    main()
