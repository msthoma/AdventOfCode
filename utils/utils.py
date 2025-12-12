import functools
import os
import sys
import time
from pathlib import Path

import aocd


def get_data(year: int = None, day: int = None):
    if year is None or day is None:
        year, day = get_year_day()
    return aocd.get_data(get_session_id(), year=year, day=day)


@functools.lru_cache
def get_session_id():
    # follow these steps to get session id:
    # https://github.com/wimglenn/advent-of-code-wim/issues/1
    # put it in a file called "session_id" in AdventOfCode folder, remove session=
    s_id_file = Path.cwd().parent / "session_id"
    assert s_id_file.is_file(), s_id_file
    with open(s_id_file, "r") as f:
        s_id = f.read()
    return s_id


def get_year_day():
    return map(int, get_script_file_name().split("_"))


def get_script_file_name():
    return Path(sys.argv[0]).stem


def input_fp(day):
    return os.path.join("inputs", f"{day}.txt")


def res_print(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)


def res_print2(res, part: int, start_time: float = None):
    total_time = (
        f" (total time: {round(time.time() - start_time, 4)}s)"
        if start_time is not None
        else ""
    )
    print(f"{get_script_file_name()} part {part} answer: {res}{total_time}", flush=True)
