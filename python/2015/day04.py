import hashlib


def main():
    partOne()
    partTwo()

def partOne():
    input = "yzbqklnj"
    i = 0
    while True:
        newInput = input + str(i)
        m = hashlib.md5()
        m.update(newInput.encode('UTF-8'))
        test = m.hexdigest()
        if test[:5] == "00000":
            break
        i += 1
    print(i)

def partTwo():
    input = "yzbqklnj"
    i = 0
    while True:
        newInput = input + str(i)
        m = hashlib.md5()
        m.update(newInput.encode('UTF-8'))
        test = m.hexdigest()
        if test[:6] == "000000":
            break
        i += 1
    print(i)

if __name__ == '__main__':
    main()