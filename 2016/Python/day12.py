def main():
    partOne()
    partTwo()


def findRegisters(registers):
    file = open("Inputs/12.txt", "r")
    lines = file.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip().split(" ")
        instruction = line[0]
        match instruction:
            case "cpy":
                origin = line[1]
                destination = line[2]
                if origin.isnumeric():
                    registers[destination] = int(origin)
                else:
                    registers[destination] = registers[origin]
            case "jnz":
                condition = line[1]
                jumpLength = line[2]
                if condition.isnumeric():
                    if int(condition) != 0:
                        i += int(jumpLength)
                        continue
                else:
                    if registers[condition] != 0:
                        i += int(jumpLength)
                        continue
            case "inc":
                register = line[1]
                registers[register] += 1
            case "dec":
                register = line[1]
                registers[register] -= 1
        i += 1


def partOne():
    registers = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    }
    findRegisters(registers)
    print(registers["a"])


def partTwo():
    registers = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0
    }
    findRegisters(registers)
    print(registers["a"])


if __name__ == '__main__':
    main()
