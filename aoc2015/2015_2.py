from functools import reduce
from operator import mul

from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()

    dims = [sorted([int(d) for d in dim.split(sep="x")]) for dim in input_data.splitlines()]

    area_needed = 0
    for dim in dims:
        l, w, h = dim
        side_areas = [l * w, w * h, h * l]
        area_needed += 2 * sum(side_areas) + min(side_areas)
        # 1598415

    ribbon_needed = 0
    for dim in dims:
        ribbon_needed += 2 * (dim[0] + dim[1]) + reduce(mul, dim, 1)

    print_res(day, 1, area_needed)
    print_res(day, 1, ribbon_needed)


if __name__ == '__main__':
    main()
