import os
import sys


def get_day_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def print_res(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)
