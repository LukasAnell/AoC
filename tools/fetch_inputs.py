"""Download Advent of Code puzzle inputs into the shared inputs/ tree.

Language-agnostic: writes to <repo_root>/inputs/<year>/<day>.txt regardless
of which language(s) you're solving in.
"""
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
INPUTS_DIR = REPO_ROOT / "inputs"


def main():
    load_dotenv()
    another_loop = True
    while another_loop:
        year = int(input("What year?\n"))
        upper_bound = int(input("Up to what day? (1-25)\n"))
        if upper_bound < 1 or upper_bound > 25:
            print("Invalid day")
            continue

        for i in range(1, upper_bound + 1):
            dest_folder = INPUTS_DIR / str(year)
            file_path = dest_folder / f"{i}.txt"
            if file_path.exists():
                continue

            fetch_input(year, i, dest_folder, file_path)
        print("Saved successfully")
        another_loop = input("Go again?\n") in ["y", "yes"]
    print("Exited.\n")


def fetch_input(year: int, day: int, dest_folder: Path, file_path: Path):
    uri = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(
        uri,
        cookies={"session": os.getenv("AOC_SESSION_COOKIE")}
    )

    dest_folder.mkdir(parents=True, exist_ok=True)

    if response.ok:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        print("Download failed: status code {}\n{}".format(response.status_code, response.text))


if __name__ == "__main__":
    main()
