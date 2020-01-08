from aoc2019.intcode import computer
from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    print_res(day, 1, computer(intcode, [1], extend=True)["output"][-1])

    print_res(day, 2, computer(intcode, [2], extend=True)["output"][-1])


if __name__ == '__main__':
    main()
