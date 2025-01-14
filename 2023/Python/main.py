import os
import requests
from hidden import SESSIONID, USER_AGENT


def main():
    for i in range(1, 26):
        fetchInputs(i)

def fetchInputs(day: int):
    uri = f"http://adventofcode.com/2023/day/{day}/input"
    response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT}, stream=True)
    dest_folder = "Inputs"
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = f"{day}.txt"
    file_path = os.path.join(dest_folder, filename)

    if response.ok:
        print("saving to", os.path.abspath(file_path))
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