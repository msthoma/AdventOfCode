import math
from collections import defaultdict

from utils.utils import res_print2, get_data


def main():
    data = get_data().splitlines()
    print(data)
    part_a, part_b = [], []

    res_print2(sum(part_a), part=1)
    res_print2(sum(part_b), part=2)


if __name__ == "__main__":
    main()
