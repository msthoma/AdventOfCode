import functools
import os
import sys
from pathlib import Path

import aocd


def get_data(year: int = None, day: int = None):
    if year is None or day is None:
        year, day = get_year_day()
    return aocd.get_data(get_session_id(), year=year, day=day)


@functools.lru_cache(100)
def get_session_id():
    s_id_file = Path.cwd().parent / "session_id"
    assert s_id_file.is_file()
    with open(s_id_file, "r") as f:
        s_id = f.read()
    return s_id


def get_year_day():
    return map(int, get_script_file_name().split("_"))


def get_script_file_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def input_fp(day):
    return os.path.join("inputs", f"{day}.txt")


def res_print(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)


def res_print2(res, part):
    print(f"{get_script_file_name()} part {part}: {res}", flush=True)
