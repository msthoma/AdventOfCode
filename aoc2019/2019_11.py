from aoc2019.intcode import computer
from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    print(intcode)


if __name__ == '__main__':
    main()
