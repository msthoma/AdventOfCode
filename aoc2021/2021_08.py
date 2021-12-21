import time

from utils.utils import res_print2, get_data

if __name__ == '__main__':
    digits = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }
    data = [[p.split(" ") for p in line.split(" | ")] for line in get_data().splitlines()]

    start = time.time()
    p1 = sum(sum(len(o) in [2, 4, 3, 7] for o in outputs) for _, outputs in data)
    res_print2(p1, 1, start)
