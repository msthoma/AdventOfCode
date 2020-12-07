import functools
import os
import sys
from pathlib import Path

import aocd


def data(year: int, day: int):
    return aocd.get_data(session_id(), year, day)


@functools.lru_cache(100)
def session_id():
    s_id_file = Path.cwd() / "session_id"
    assert s_id_file.is_file()
    with open(s_id_file, "r") as f:
        s_id = f.read()
    return s_id


def day_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def input_fp(day):
    return os.path.join("inputs", f"{day}.txt")


def print_res(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)
