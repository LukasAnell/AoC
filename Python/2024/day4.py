import regex as re


def main():
    partOne()
    partTwo()


def rotate45Degrees(arr):
    n = len(arr)
    m = len(arr[0])
    rotated = [[] for _ in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            rotated[i + j].append(arr[i][j])
    return rotated


def partOne():
    file = open("Inputs/4.txt", "r")
    normalRotation = [[char for char in line.strip()] for line in file]
    sidewaysRotation = [list(row) for row in zip(*normalRotation[::-1])]
    diagonalRotation1 = rotate45Degrees(normalRotation)
    diagonalRotation2 = rotate45Degrees(normalRotation[::-1])
    pattern = re.compile(r"XMAS|SAMX")
    total = 0
    for rotation in [normalRotation, sidewaysRotation, diagonalRotation1, diagonalRotation2]:
        for i in range(len(rotation)):
            line = "".join(rotation[i])
            matches = pattern.findall(line, overlapped=True)
            total += len(matches)
    print(total)


def partTwo():
    file = open('Inputs/4.txt', 'r')
    lines = [line.strip() for line in file]
    count = 0
    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            if lines[r][c] == 'A':
                firstDiag = lines[r - 1][c - 1] + lines[r][c] + lines[r + 1][c + 1]
                secondDiag = lines[r + 1][c - 1] + lines[r][c] + lines[r - 1][c + 1]
                if (firstDiag == "MAS" or firstDiag == "SAM") and (secondDiag == "MAS" or secondDiag == "SAM"):
                    count += 1
    print(count)


if __name__ == "__main__":
    main()