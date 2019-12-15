from itertools import permutations

from aoc2019.intcode import computer
from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    comb_dict = {}
    for comb in permutations(range(5)):
        input_signal = 0
        for phase in comb:
            res = list(computer(intcode.copy(), [phase, input_signal]))
            input_signal = res[-1]
        comb_dict[comb] = input_signal

    print_res(day, 1, max(comb_dict.values()))


if __name__ == '__main__':
    main()
