from utils.utils import day_name, input_fp, print_res
from aoc2019.intcode import computer


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]
    print(list(computer(intcode, 1)))


if __name__ == '__main__':
    main()
