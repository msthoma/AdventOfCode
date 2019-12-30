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

    asteroid_los = {}

    for station in asteroid_coords:
        in_los = set()

        for asteroid in asteroid_coords:
            if asteroid != station:
                dx, dy = np.array(asteroid) - np.array(station)
                gcd = abs(math.gcd(dx, dy))
                in_los.add((dx // gcd, dy // gcd))

        asteroid_los[tuple(station)] = len(in_los)

        # a = np.array(a)
        # # euclidean distances with other asteroids
        # a_eucl = {}
        # for b in asteroid_coord:
        #     b = np.array(b)
        #     if np.array_equal(a, b):
        #         continue
        #     eucl_d = norm(a - b)
        #     # center at a (by b - a) and find angle of b from center - https://en.wikipedia.org/wiki/Atan2
        #     angle = np.arctan2(*(b - a))
        #     # ab = np.dot(a, b)
        #     # normab = norm(a) * norm(b)
        #     # line_angle = np.arccos((a @ b) / (norm(a) * norm(b)))
        #     manhattan = list(np.absolute(a - b))
        #     a_eucl[tuple(b)] = {"eucl": eucl_d, "angle": angle}
        #
        # a_eucl = {k: v for k, v in sorted(a_eucl.items(), key=lambda item: item[1]["eucl"])}
        # print(a_eucl)
        #
        # angles = [v["angle"] for k, v in a_eucl.items()]
        # print(sorted(angles))
        # for asteroid, val in a_eucl.items():
        #     pass

        # asteroids in line of sight of a
        # in_line = []
        # blocked_lines = []
        # ax, ay = a
        # for bx, by in a_eucl:
        #     if not in_line:
        #         in_line.append([bx, by])
        #         blocked_lines.append([bx, by])
        # print(in_line)
        # print(10 % 0)
    max_los = max(asteroid_los, key=asteroid_los.get)

    print_res(day, 1, asteroid_los[max_los])


if __name__ == '__main__':
    main()
