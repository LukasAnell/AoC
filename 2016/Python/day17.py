import hashlib
from collections import deque


def main():
    partOne()
    partTwo()


def getPasscode():
    file = open("Inputs/17.txt", "r")
    return [line.strip() for line in file][0]


def getOpenDoors(passcode, path):
    hash = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
    return [c in 'bcdef' for c in hash]


def bfs(passcode):
    directions = ['U', 'D', 'L', 'R']
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([((0, 0), "")])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == (3, 3):
            return path
        openDoors = getOpenDoors(passcode, path)
        for i, (dx, dy) in enumerate(moves):
            if openDoors[i]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    queue.append(((nx, ny), path + directions[i]))
    return None


def partOne():
    print(bfs(getPasscode()))


def partTwo():
    passcode = getPasscode()
    directions = ['U', 'D', 'L', 'R']
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([((0, 0), "")])
    longestPath = ""
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == (3, 3):
            longestPath = path
            continue
        openDoors = getOpenDoors(passcode, path)
        for i, (dx, dy) in enumerate(moves):
            if openDoors[i]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    queue.append(((nx, ny), path + directions[i]))
    print(len(longestPath))


if __name__ == "__main__":
    main()
