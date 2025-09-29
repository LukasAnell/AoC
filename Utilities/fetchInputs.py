import os
import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    another_loop = True
    while (another_loop):
        year = int(input("What year?\n"))
        for i in range(1, 25 + 1):
            fetchInputs(year, i)
        print("Saved successfully")
        another_loop = input("Go again?\n") in ["y", "yes"]
    print("Exited.\n")


def fetchInputs(year: int, day: int):
    uri = f"http://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(uri, cookies={'session': os.getenv("SESSION_ID")},
                            headers={'User-Agent': os.getenv("USER_AGENT")}, stream=True)
    dest_folder = f"../{year}/Inputs"
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = f"{day}.txt"
    file_path = os.path.join(dest_folder, filename)

    if response.ok:
        # print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        print("Download failed: status code {}\n{}".format(response.status_code, response.text))


if __name__ == '__main__':
    main()
