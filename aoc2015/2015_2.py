from functools import reduce
from operator import mul

from utils.utils import res_print2, get_data


def main():
    input_data = get_data()

    dims = [sorted([int(d) for d in dim.split(sep="x")]) for dim in
            input_data.splitlines()]

    area_needed = 0
    for dim in dims:
        l, w, h = dim
        side_areas = [l * w, w * h, h * l]
        area_needed += 2 * sum(side_areas) + min(side_areas)

    ribbon_needed = 0
    for dim in dims:
        ribbon_needed += 2 * (dim[0] + dim[1]) + reduce(mul, dim, 1)

    res_print2(area_needed, 1)
    res_print2(ribbon_needed, 2)


if __name__ == '__main__':
    main()
