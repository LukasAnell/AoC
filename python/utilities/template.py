"""Copy this file to python/<year>/dayNN.py to start a new day."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import read_input_lines

lines = read_input_lines()


def main():
    part_one()
    part_two()


def part_one():
    pass


def part_two():
    pass


if __name__ == "__main__":
    main()
