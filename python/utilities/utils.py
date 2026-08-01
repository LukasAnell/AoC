"""Shared helpers for Python Advent of Code solutions."""
import inspect
from pathlib import Path

# python/utilities/utils.py -> repo root is two levels up
REPO_ROOT = Path(__file__).resolve().parents[2]
INPUTS_DIR = REPO_ROOT / "inputs"


def read_input_lines(year=None, day=None):
    """Read the puzzle input for `year`/`day` as a list of lines (with line endings).

    If `year`/`day` are omitted, they're inferred from the caller's file path,
    which is expected to look like `python/<year>/dayNN.py`. Works regardless
    of the current working directory the script is launched from.
    """
    if year is None or day is None:
        caller_path = Path(inspect.currentframe().f_back.f_code.co_filename).resolve()
        year = year if year is not None else caller_path.parent.name
        day = day if day is not None else caller_path.stem.removeprefix("day").lstrip("0")

    day = str(int(day))  # normalize "01"/"1" -> "1" to match fetched input filenames
    input_file = INPUTS_DIR / str(year) / f"{day}.txt"
    return input_file.read_text().splitlines(keepends=True)


def read_input_text(year=None, day=None):
    """Same as read_input_lines but returns the raw input as a single string."""
    if year is None or day is None:
        caller_path = Path(inspect.currentframe().f_back.f_code.co_filename).resolve()
        year = year if year is not None else caller_path.parent.name
        day = day if day is not None else caller_path.stem.removeprefix("day").lstrip("0")

    day = str(int(day))
    input_file = INPUTS_DIR / str(year) / f"{day}.txt"
    return input_file.read_text()
