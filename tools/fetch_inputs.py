import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
INPUTS_DIR = REPO_ROOT / "inputs"


def main() -> None:
    load_dotenv()

    session_cookie = os.getenv("AOC_SESSION_COOKIE")
    if not session_cookie:
        sys.exit(
            "AOC_SESSION_COOKIE is not set. Copy .env.example to .env and fill it in."
        )

    another_loop = True
    while another_loop:
        year = int(input("What year?\n"))
        upper_bound = int(input("Up to what day? (1-25)\n"))
        if upper_bound < 1 or upper_bound > 25:
            print("Invalid day")
            continue

        for day in range(1, upper_bound + 1):
            dest_folder = INPUTS_DIR / str(year)
            file_path = dest_folder / f"{day}.txt"
            if file_path.exists():
                continue

            fetch_input(year, day, dest_folder, file_path, session_cookie)

        print("Saved successfully")
        another_loop = input("Go again?\n").strip().lower() in ["y", "yes"]
    print("Exited.\n")


def fetch_input(
    year: int, day: int, dest_folder: Path, file_path: Path, session_cookie: str
) -> None:
    uri = f"https://adventofcode.com/{year}/day/{day}/input"

    try:
        response = requests.get(uri, cookies={"session": session_cookie}, timeout=10)
    except requests.RequestException as e:
        print(f"Request failed for {year} day {day}: {e}")
        return

    if not response.ok:
        print(
            f"Download failed for {year} day {day}: status {response.status_code}\n{response.text}"
        )
        return

    dest_folder.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())


if __name__ == "__main__":
    main()
