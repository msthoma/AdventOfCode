import os
import sys
from functools import reduce
from operator import mul

day_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]


def main():
    with open(f"{day_name}.txt", "r") as f:
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

    print(f"{day_name}_1 answer:", area_needed)
    print(f"{day_name}_2 answer:", ribbon_needed)


if __name__ == '__main__':
    main()
