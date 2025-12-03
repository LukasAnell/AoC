def main():
    partOne()
    partTwo()


def getBotsLowsHighs():
    file = open("Inputs/10.txt", "r")
    bots = {}
    lows = {}
    highs = {}
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "value":
            value = int(line[1])
            botNum = int(line[5])
            if botNum in bots.keys():
                bots[botNum] = bots.get(botNum) + [value]
            else:
                bots[botNum] = [value]
        elif line[0] == "bot":
            initialNum = int(line[1])
            lowNum = int(line[6])
            highNum = int(line[11])
            lows[initialNum] = (line[5] == "output", lowNum)
            highs[initialNum] = (line[10] == "output", highNum)
    return bots, lows, highs


def partOne():
    bots, lows, highs = getBotsLowsHighs()
    while True:
        for bot, values in bots.items():
            if len(values) == 2:
                lowValue, highValue = sorted(values)
                if lowValue == 17 and highValue == 61:
                    print(bot)
                    return
                lowIsOutput, lowNum = lows[bot]
                highIsOutput, highNum = highs[bot]
                if not lowIsOutput:
                    if lowNum in bots:
                        bots[lowNum].append(lowValue)
                    else:
                        bots[lowNum] = [lowValue]
                if not highIsOutput:
                    if highNum in bots:
                        bots[highNum].append(highValue)
                    else:
                        bots[highNum] = [highValue]
                bots[bot] = []
                break


def partTwo():
    bots, lows, highs = getBotsLowsHighs()
    outputs = {}
    while True:
        for bot, values in bots.items():
            if len(values) == 2:
                lowValue, highValue = sorted(values)
                lowIsOutput, lowNum = lows[bot]
                highIsOutput, highNum = highs[bot]
                if not lowIsOutput:
                    if lowNum in bots:
                        bots[lowNum].append(lowValue)
                    else:
                        bots[lowNum] = [lowValue]
                else:
                    outputs[lowNum] = lowValue
                if not highIsOutput:
                    if highNum in bots:
                        bots[highNum].append(highValue)
                    else:
                        bots[highNum] = [highValue]
                else:
                    outputs[highNum] = highValue
                bots[bot] = []
                break
        if 0 in outputs and 1 in outputs and 2 in outputs:
            print(outputs[0] * outputs[1] * outputs[2])
            return


if __name__ == '__main__':
    main()