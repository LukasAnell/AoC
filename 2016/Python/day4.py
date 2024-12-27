def main():
    partOne()
    partTwo()


def getRooms():
    file = open("Inputs/4.txt", "r")
    rooms = []
    for line in file:
        line = line.strip()
        encryptedName = ''.join(line.split("-")[:-1])
        sectorId = int(line.split("-")[-1].split("[")[0])
        checksum = line.split("[")[1][:-1]
        rooms.append([encryptedName, sectorId, checksum])
    return rooms


def mostCommonLetters(encryptedName):
    letterCount = set()
    for char in encryptedName:
        letterCount.add((char, encryptedName.count(char)))
    return [pair[0] for pair in sorted(list(letterCount), key=lambda x: (-x[1], x[0]))[:5]]


def partOne():
    rooms = getRooms()
    sumSectorIds = 0
    for room in rooms:
        if ''.join(mostCommonLetters(room[0])) == room[2]:
            sumSectorIds += room[1]
    print(sumSectorIds)


def shiftLetter(letter, amount):
    return chr((ord(letter) - 97 + amount) % 26 + 97)


def partTwo():
    realRooms = []
    for room in getRooms():
        if ''.join(mostCommonLetters(room[0])) == room[2]:
            realRooms.append(room)
    for room in realRooms:
        encryptedName = room[0].replace("-", " ")
        sectorId = room[1]
        newName = ""
        for char in encryptedName:
            newName += shiftLetter(char, sectorId)
        if "north" in newName:
            print(sectorId)
            break


if __name__ == '__main__':
    main()