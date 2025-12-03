import heapq
from functools import cache


def main():
    partOne()
    partTwo()


def isValidState(floors):
    for floor in floors:
        generators = {item[0] for item in floor if item[1] == 'G'}
        microchips = {item[0] for item in floor if item[1] == 'M'}
        if generators and microchips - generators:
            return False
    return True


def getNextStates(state):
    floors, elevator = state
    currentFloor = floors[elevator]
    nextStates = []
    for i in range(len(currentFloor)):
        for j in range(i, len(currentFloor)):
            for direction in [-1, 1]:
                newElevator = elevator + direction
                if 0 <= newElevator < len(floors):
                    newFloors = [list(floor) for floor in floors]
                    newFloors[elevator].remove(currentFloor[i])
                    if i != j:
                        newFloors[elevator].remove(currentFloor[j])
                    newFloors[newElevator].append(currentFloor[i])
                    if i != j:
                        newFloors[newElevator].append(currentFloor[j])
                    if isValidState(newFloors):
                        nextStates.append((tuple(tuple(floor) for floor in newFloors), newElevator))
    return nextStates


def serializeState(state):
    floors, elevator = state
    return tuple(tuple(sorted(floor)) for floor in floors), elevator


def heuristic(state):
    floors, _ = state
    return sum(3 - i for i, floor in enumerate(floors) for _ in floor)


@cache
def bfs(initialState):
    queue = []
    heapq.heappush(queue, (0, initialState, 0))
    visited = set()
    visited.add(serializeState(initialState))
    while queue:
        _, state, steps = heapq.heappop(queue)
        floors, elevator = state
        if all(len(floor) == 0 for floor in floors[:-1]) and len(floors[-1]) == sum(len(floor) for floor in floors):
            return steps
        for nextState in getNextStates(state):
            serializedState = serializeState(nextState)
            if serializedState not in visited:
                visited.add(serializedState)
                priority = steps + 1 + heuristic(nextState)
                heapq.heappush(queue, (priority, nextState, steps + 1))
    return -1


def parseInput():
    file = open("Inputs/11.txt", "r")
    floors = []
    for line in file:
        line = line.strip().split(" a ")
        floor = []
        for item in line[1:]:
            if "generator" in item:
                floor.append(item.split()[0][0].upper() + "G")
            elif "microchip" in item:
                floor.append(item.split()[0][0].upper() + "M")
        floors.append(floor)
    return floors


def partOne():
    floors = parseInput()
    initialState = (tuple(tuple(floor) for floor in floors), 0)
    print(bfs(initialState))


def partTwo():
    floors = parseInput()
    floors[0] += ["EG", "EM", "DG", "DM"]
    initialState = (tuple(tuple(floor) for floor in floors), 0)
    print(bfs(initialState))


if __name__ == '__main__':
    main()
