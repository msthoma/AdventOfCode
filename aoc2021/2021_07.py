import time
from collections import defaultdict

from utils.utils import res_print2, get_data


def triangular_number(n: int) -> int:
    return n * (n + 1) // 2


if __name__ == '__main__':
    data = sorted(map(int, get_data().split(",")))

    for i, fuel_equation in enumerate([lambda c, p: abs(c - p), lambda c, p: triangular_number(abs(c - p))], start=1):
        start = time.time()
        min_fuel_so_far, fuel_per_position = 0, defaultdict(int)
        for position in range(max(data) + 1):
            for crab in data:
                fuel_per_position[position] += fuel_equation(crab, position)
                if position > 0 and fuel_per_position[position] >= min_fuel_so_far:
                    break  # stop early if min fuel is exceeded
            if position == 0:
                min_fuel_so_far = fuel_per_position[position]
            if (new_min := fuel_per_position[position]) < min_fuel_so_far:
                min_fuel_so_far = new_min
        res_print2(min_fuel_so_far, i, start)
