import re
from collections import defaultdict
from functools import lru_cache
from itertools import product

from utils.utils import get_data, res_print2


@lru_cache(1000)
def get_combinations(num_x: int):
    return list(product(range(2), repeat=num_x))


def get_address_combinations(mask: str, address: int):
    address = str(format(address, "b"))
    address = "000000000000000000000000000000000"[:36 - len(address)] + address
    masked = ""
    for a, m in zip(address, mask):
        if m == "X":
            masked += m
        elif m == "1":
            masked += m
        else:
            masked += a
    address_combinations = []
    for cbn in get_combinations(mask.count("X")):
        floating = masked
        for bit in cbn:
            floating = floating.replace("X", str(bit), 1)
        address_combinations.append(int(floating, 2))
    return address_combinations


def apply_mask(mask: str, num: int):
    num = str(format(num, "b"))
    num = "000000000000000000000000000000000"[:36 - len(num)] + num
    num = "".join(m if m.isdigit() else n for n, m in zip(num, mask))
    return int(num, 2)


def main():
    data = get_data().splitlines()

    pat = re.compile(r"mem\[(\d+)] = (\d+)$")

    # part a
    mem = defaultdict(int)
    mask = ""
    for line in data:
        if "mask" in line:
            mask = line.replace("mask = ", "")
            continue
        else:
            a, v = pat.match(line).groups()
            address, val = int(a), int(v)
        assert address != 0
        mem[address] = apply_mask(mask, val)

    res_print2(sum(mem.values()), 1)

    # part b
    mem_2 = defaultdict(int)
    mask_2 = ""
    for line in data:
        if "mask" in line:
            mask_2 = line.replace("mask = ", "")
            continue
        else:
            a, v = pat.match(line).groups()
            address, val = int(a), int(v)
        assert address != 0
        for comb_address in get_address_combinations(mask_2, address):
            mem_2[comb_address] = val

    res_print2(sum(mem_2.values()), 2)


if __name__ == '__main__':
    main()
