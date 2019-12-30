import math

import numpy as np

from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()
    asteroid_map = np.array([[1 if s == "#" else 0 for s in line.strip()] for line in input_data])

    asteroid_coords = []

    for y in range(asteroid_map.shape[0]):
        for x in range(asteroid_map.shape[1]):
            if asteroid_map[y, x] == 1:
                asteroid_coords.append([x, y])

    asteroid_max_los = {}
    asteroid_los = {}

    for station in asteroid_coords:
        in_los = set()

        for asteroid in asteroid_coords:
            if asteroid != station:
                dx, dy = np.array(asteroid) - np.array(station)
                gcd = abs(math.gcd(dx, dy))
                in_los.add((dx // gcd, dy // gcd))

        asteroid_los[tuple(station)] = in_los
        asteroid_max_los[tuple(station)] = len(in_los)

    max_los = max(asteroid_max_los, key=asteroid_max_los.get)

    print_res(day, 1, asteroid_max_los[max_los])


if __name__ == '__main__':
    main()
