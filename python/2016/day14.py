import hashlib
import re

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "utilities"))
from utils import INPUTS_DIR

INPUT_FILE = INPUTS_DIR / "2016" / "14.txt"


def main():
    partOne()
    partTwo()


def partOne():
    file = open(INPUT_FILE)
    salt = [line.strip() for line in file][0]
    i = 0
    keys = []
    hashCache = {}
    def get_hash(index):
        if index not in hashCache:
            hashCache[index] = hashlib.md5((salt + str(index)).encode('UTF-8')).hexdigest()
        return hashCache[index]
    while len(keys) < 64:
        currentHash = get_hash(i)
        tripletMatch = re.search(r'(.)\1\1', currentHash)
        if tripletMatch:
            tripletChar = tripletMatch.group(1)
            for j in range(i + 1, i + 1001):
                if tripletChar * 5 in get_hash(j):
                    keys.append(i)
                    break
        i += 1
    print(keys[63])


def partTwo():
    file = open(INPUT_FILE)
    salt = [line.strip() for line in file][0]
    i = 0
    keys = []
    hashCache = {}
    def get_hash(index):
        if index not in hashCache:
            hashCache[index] = hashlib.md5((salt + str(index)).encode('UTF-8')).hexdigest()
            for _ in range(2016):
                hashCache[index] = hashlib.md5(hashCache[index].encode('UTF-8')).hexdigest()
        return hashCache[index]
    while len(keys) < 64:
        currentHash = get_hash(i)
        tripletMatch = re.search(r'(.)\1\1', currentHash)
        if tripletMatch:
            tripletChar = tripletMatch.group(1)
            for j in range(i + 1, i + 1001):
                if tripletChar * 5 in get_hash(j):
                    keys.append(i)
                    break
        i += 1
    print(keys[63])


if __name__ == '__main__':
    main()