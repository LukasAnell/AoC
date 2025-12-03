def main():
    partOne()
    partTwo()


def findHypernetsAndOutsides(line):
    hypernets = []
    outsides = []
    segments = line.replace('[', ']').split(']')
    for i, segment in enumerate(segments):
        if i % 2 == 0:
            outsides.append(segment)
        else:
            hypernets.append(segment)
    return hypernets, outsides


def hasABBA(characterList):
    for i in range(len(characterList)):
        for j in range(len(characterList[i]) - 3):
            if characterList[i][j] == characterList[i][j + 3] and characterList[i][j + 1] == characterList[i][j + 2] and characterList[i][j] != characterList[i][j + 1]:
                return True
    return False


def partOne():
    file = open("Inputs/7.txt", "r")
    supportTLSCount = 0
    for line in file:
        line = line.strip()
        hypernets, outsides = findHypernetsAndOutsides(line)
        if hasABBA(outsides) and not hasABBA(hypernets):
            supportTLSCount += 1
    print(supportTLSCount)


def findABA(segment):
    abaList = []
    for i in range(len(segment) - 2):
        if segment[i] == segment[i + 2] and segment[i] != segment[i + 1]:
            abaList.append(segment[i:i + 3])
    return abaList


def hasCorrespondingBAB(aba_list, hypernets):
    for aba in aba_list:
        bab = aba[1] + aba[0] + aba[1]
        for hypernet in hypernets:
            if bab in hypernet:
                return True
    return False


def partTwo():
    file = open("Inputs/7.txt", "r")
    supportSSLCount = 0
    for line in file:
        line = line.strip()
        hypernets, outsides = findHypernetsAndOutsides(line)
        abaList = []
        for outside in outsides:
            abaList.extend(findABA(outside))
        if hasCorrespondingBAB(abaList, hypernets):
            supportSSLCount += 1
    print(supportSSLCount)


if __name__ == "__main__":
    main()
