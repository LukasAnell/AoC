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
                low_value, high_value = sorted(values)
                if low_value == 17 and high_value == 61:
                    print(bot)
                    return
                low_is_output, low_num = lows[bot]
                high_is_output, high_num = highs[bot]
                if not low_is_output:
                    if low_num in bots:
                        bots[low_num].append(low_value)
                    else:
                        bots[low_num] = [low_value]
                if not high_is_output:
                    if high_num in bots:
                        bots[high_num].append(high_value)
                    else:
                        bots[high_num] = [high_value]
                bots[bot] = []
                break


def partTwo():
    bots, lows, highs = getBotsLowsHighs()
    outputs = {}
    while True:
        for bot, values in bots.items():
            if len(values) == 2:
                low_value, high_value = sorted(values)
                low_is_output, low_num = lows[bot]
                high_is_output, high_num = highs[bot]
                if not low_is_output:
                    if low_num in bots:
                        bots[low_num].append(low_value)
                    else:
                        bots[low_num] = [low_value]
                else:
                    outputs[low_num] = low_value
                if not high_is_output:
                    if high_num in bots:
                        bots[high_num].append(high_value)
                    else:
                        bots[high_num] = [high_value]
                else:
                    outputs[high_num] = high_value
                bots[bot] = []
                break
        if 0 in outputs and 1 in outputs and 2 in outputs:
            print(outputs[0] * outputs[1] * outputs[2])
            return


if __name__ == '__main__':
    main()