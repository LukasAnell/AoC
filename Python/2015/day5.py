def main():
    partOne()
    partTwo()

def partOne():
    file = open("Inputs/5.txt", "r")
    vowels = ['a', 'e', 'i', 'o', 'u']
    strings = ["ab", "cd", "pq", "xy"]
    niceStrings = 0
    for line in file:
        line = line.strip()
        numVowels = 0
        hasDouble = False
        noString = True
        for char in line:
            if char in vowels:
                numVowels += 1
        for s in strings:
            if s in line:
                noString = False
                break
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                hasDouble = True
                break
        if numVowels >= 3 and hasDouble and noString:
            niceStrings += 1
    print(niceStrings)

def partTwo():
    file = open("Inputs/5.txt", "r")
    niceStrings = 0
    for line in file:
        containsPair = False
        repeatBetween = False
        for i in range(1, len(line) - 1):
            if line[i - 1] == line[i + 1]:
                repeatBetween = True
                break
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line) - 1):
                if i + 1 != j and line[i : i + 2] == line[j : j + 2]:
                    containsPair = True
                    break
            if containsPair:
                break
        if repeatBetween and containsPair:
            niceStrings += 1
    print(niceStrings)


if __name__ == '__main__':
    main()