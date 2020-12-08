import functools
import os
import sys
from pathlib import Path

import aocd


def data(year: int = None, day: int = None):
    if year is None or day is None:
        year, day = get_year_day()
    return aocd.get_data(session_id(), year=year, day=day)


@functools.lru_cache(100)
def session_id():
    s_id_file = Path.cwd().parent / "session_id"
    assert s_id_file.is_file()
    with open(s_id_file, "r") as f:
        s_id = f.read()
    return s_id


def get_year_day():
    return map(int, day_name().split("_"))


def day_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def input_fp(day):
    return os.path.join("inputs", f"{day}.txt")


def print_res(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)
