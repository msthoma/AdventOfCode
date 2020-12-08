from aoc2019.intcode import computer
from utils.utils import get_script_file_name, input_fp, res_print


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    res_print(day, 1, computer(intcode, [1], extend=True)["output"][-1])

    res_print(day, 2, computer(intcode, [2], extend=True)["output"][-1])


if __name__ == '__main__':
    main()
