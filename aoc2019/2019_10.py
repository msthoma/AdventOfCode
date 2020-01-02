import math

import numpy as np

from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()
    asteroid_map = np.array([[1 if s == "#" else 0 for s in line.strip()] for line in input_data])

    asteroid_coords = []

    for x in range(asteroid_map.shape[0]):
        for y in range(asteroid_map.shape[1]):
            if asteroid_map[x, y] == 1:
                asteroid_coords.append([x, y])

    # part 1
    los_asteroid_counts = {}
    los_asteroids_rel = {}

    for station in asteroid_coords:
        in_los = set()

        for asteroid in asteroid_coords:
            if asteroid != station:
                dx, dy = np.array(asteroid) - np.array(station)
                gcd = abs(math.gcd(dx, dy))
                in_los.add((dx // gcd, dy // gcd))

        los_asteroids_rel[tuple(station)] = in_los
        los_asteroid_counts[tuple(station)] = len(in_los)

    station = max(los_asteroid_counts, key=los_asteroid_counts.get)

    print_res(day, 1, los_asteroid_counts[station])

    # part 2
    los_angles = {math.atan2(y, x): (x, y) for x, y in los_asteroids_rel[station]}

    asteroid_200th = los_angles[sorted(los_angles.keys(), reverse=True)[200 - 1]]
    dx, dy = asteroid_200th

    x, y = station[0] + dx, station[1] + dy

    while [x, y] not in asteroid_coords:
        x, y = x + dx, y + dy

    print_res(day, 2, y * 100 + x)


if __name__ == '__main__':
    main()
