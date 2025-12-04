import inspect


def readInputLines():
    callerFilename = inspect.currentframe().f_back.f_code.co_filename
    year = callerFilename.split("\\")[-2]
    day = callerFilename.split("\\")[-1].split(".")[0][3:]

    return open(f"../../Inputs/{year}/{day}.txt").readlines()
