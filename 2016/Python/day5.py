import hashlib


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/5.txt", "r")
    doorId = [line.strip() for line in file][0]
    i = 0
    times = 0
    password = ""
    while times < 8:
        newDoorId = doorId + str(i)
        m = hashlib.md5()
        m.update(newDoorId.encode('UTF-8'))
        test = m.hexdigest()
        if test[:5] == "00000":
            password += test[5]
            times += 1
        i += 1
    print(password)


def partTwo():
    file = open("Inputs/5.txt", "r")
    doorId = [line.strip() for line in file][0]
    i = 0
    times = 0
    password = ['_'] * 8
    while times < 8:
        newDoorId = doorId + str(i)
        m = hashlib.md5()
        m.update(newDoorId.encode('UTF-8'))
        test = m.hexdigest()
        if test[:5] == "00000":
            if test[5].isdigit() and int(test[5]) < 8 and password[int(test[5])] == '_':
                password[int(test[5])] = test[6]
                times += 1
        i += 1
    print(''.join([str(char) for char in password]))


if __name__ ==  '__main__':
    main()