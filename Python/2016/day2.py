def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/2.txt", "r")
    instructions = [line.strip() for line in file]
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    code = ""
    pos = [1, 1]
    for instr in instructions:
        for i in range(len(instr)):
            direction = instr[i]
            if direction == 'U' and pos[0] - 1 >= 0:
                pos[0] -= 1
            elif direction == 'R' and pos[1] + 1 <= 2:
                pos[1] += 1
            elif direction == 'D' and pos[0] + 1 <= 2:
                pos[0] += 1
            elif direction == 'L' and pos[1] - 1 >= 0:
                pos[1] -= 1
        code += str(keypad[pos[0]][pos[1]])
    print(code)


def partTwo():
    file = open("Inputs/2.txt", "r")
    instructions = [line.strip() for line in file]
    keypad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0]
    ]
    code = ""
    pos = [2, 0]
    for instr in instructions:
        for i in range(len(instr)):
            direction = instr[i]
            if direction == 'U' and pos[0] - 1 >= 0 and keypad[pos[0] - 1][pos[1]] != 0:
                pos[0] -= 1
            elif direction == 'R' and pos[1] + 1 <= 4 and keypad[pos[0]][pos[1] + 1] != 0:
                pos[1] += 1
            elif direction == 'D' and pos[0] + 1 <= 4 and keypad[pos[0] + 1][pos[1]] != 0:
                pos[0] += 1
            elif direction == 'L' and pos[1] - 1 >= 0 and keypad[pos[0]][pos[1] - 1] != 0:
                pos[1] -= 1
        code += str(keypad[pos[0]][pos[1]])
    print(code)


if __name__ == '__main__':
    main()