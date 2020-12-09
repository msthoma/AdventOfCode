import re

import numpy as np

from utils.utils import get_data, res_print2


def main():
    pat = re.compile(r"(.+) (\d+,\d+) .+ (\d+,\d+)")
    data = [list(pat.match(inst).groups()) for inst in get_data().splitlines()]
    split_ints = lambda x: tuple(map(int, x.split(",")))
    data = [[i[0], split_ints(i[1]), split_ints(i[2])] for i in data]

    lights_1 = np.zeros((1000, 1000)).astype("int8")
    lights_2 = lights_1.copy()

    for instr, c1, c2 in data:
        area1 = lights_1[c1[0]:c2[0] + 1, c1[1]:c2[1] + 1]
        area2 = lights_2[c1[0]:c2[0] + 1, c1[1]:c2[1] + 1]
        if instr == "toggle":
            lights_1[c1[0]:c2[0] + 1, c1[1]:c2[1] + 1] = 1 - area1
            area2 += 2
        elif instr == "turn on":
            lights_1[c1[0]:c2[0] + 1, c1[1]:c2[1] + 1] = 1
            area2 += 1
        elif instr == "turn off":
            lights_1[c1[0]:c2[0] + 1, c1[1]:c2[1] + 1] = 0
            area2[area2 > 0] -= 1
        else:
            raise ValueError

    res_print2(lights_1.sum(), 1)
    res_print2(lights_2.sum(), 2)


if __name__ == '__main__':
    main()
