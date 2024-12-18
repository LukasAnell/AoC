def main():
    partOne()
    partTwo()


def getReindeerStats():
    file = open("Inputs/14.txt", "r")
    lines = [line.strip().split() for line in file]
    reindeerStats = {}
    for line in lines:
        name = line[0]
        speed = int(line[3])
        flyTime = int(line[6])
        restTime = int(line[13])
        reindeerStats[name] = (speed, flyTime, restTime)
    return reindeerStats


def partOne():
    reindeerStats = getReindeerStats()
    time = 2503
    maxDistance = 0
    for reindeer in reindeerStats:
        speed, flyTime, restTime = reindeerStats[reindeer]
        distance = (time // (flyTime + restTime)) * flyTime * speed
        distance += min(flyTime, time % (flyTime + restTime)) * speed
        maxDistance = max(maxDistance, distance)
    print(maxDistance)


def partTwo():
    reindeerStats = getReindeerStats()
    time = 2503
    scores = {}
    for reindeer in reindeerStats:
        scores[reindeer] = 0
    for t in range(1, time + 1):
        maxDistance = 0
        for reindeer in reindeerStats:
            speed, flyTime, restTime = reindeerStats[reindeer]
            distance = (t // (flyTime + restTime)) * flyTime * speed
            distance += min(flyTime, t % (flyTime + restTime)) * speed
            maxDistance = max(maxDistance, distance)
        for reindeer in reindeerStats:
            speed, flyTime, restTime = reindeerStats[reindeer]
            distance = (t // (flyTime + restTime)) * flyTime * speed
            distance += min(flyTime, t % (flyTime + restTime)) * speed
            if distance == maxDistance:
                scores[reindeer] += 1
    print(max(scores.values()))


if __name__ == '__main__':
    main()