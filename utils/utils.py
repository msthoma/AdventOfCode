import os
import sys


def day_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def input_fp(day):
    return os.path.join("inputs", f"{day}.txt")


def print_res(day_name, part, res):
    print(f"{day_name}_{part} answer:", res)
