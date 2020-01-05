import re
from copy import deepcopy
from itertools import combinations

import numpy as np

from utils.utils import day_name, input_fp, print_res

dimensions = ["x", "y", "z"]
moons = ["Io", "Europa", "Ganymede", "Callisto"]


def simulate(positions, velocities):
    for moon1, moon2 in combinations(positions.keys(), 2):
        if positions[moon1] < positions[moon2]:
            velocities[moon1] += 1
            velocities[moon2] -= 1
        elif positions[moon1] > positions[moon2]:
            velocities[moon1] -= 1
            velocities[moon2] += 1

    for moon in moons:
        positions[moon] += velocities[moon]


def main():
    day = day_name()

    pattern = r"<x=(-?\d+).+y=(-?\d+).+z=(-?\d+)>"

    with open(input_fp(day), "r") as f:
        data = [re.match(pattern, line).groups() for line in f.readlines()]

    # part 1
    positions = {}
    velocities = {}

    for [x, y, z], moon in zip(data, moons):
        positions[moon] = {"x": int(x), "y": int(y), "z": int(z)}
        velocities[moon] = {"x": 0, "y": 0, "z": 0}

    for _ in range(1000):
        for moon1, moon2 in combinations(positions.keys(), 2):
            for dim in dimensions:
                if positions[moon1][dim] < positions[moon2][dim]:
                    velocities[moon1][dim] += 1
                    velocities[moon2][dim] -= 1
                elif positions[moon1][dim] > positions[moon2][dim]:
                    velocities[moon1][dim] -= 1
                    velocities[moon2][dim] += 1

        for moon in moons:
            for dim in dimensions:
                positions[moon][dim] += velocities[moon][dim]

    # calculate total energy
    total = 0
    for moon in moons:
        total += sum(abs(p) for p in positions[moon].values()) * sum(abs(v) for v in velocities[moon].values())

    print_res(day, 1, total)

    # part 2
    # arrange dictionaries based on dimension
    pos1 = {k: {} for k in dimensions}
    vel1 = {k: {} for k in dimensions}
    for i, dim in enumerate(pos1.keys()):
        for j, moon in enumerate(moons):
            pos1[dim][moon] = int(data[j][i])
            vel1[dim][moon] = 0

    # make copies to compare with original after each simulation
    pos2 = deepcopy(pos1)
    vel2 = deepcopy(vel1)

    # simulate each dimension separately, until it reaches values identical to the original
    steps_all = []
    for dim in dimensions:
        steps = 0
        while True:
            simulate(pos2[dim], vel2[dim])
            steps += 1
            if pos1[dim] == pos2[dim] and vel1[dim] == vel2[dim]:
                steps_all.append(steps)
                break

    # answer is the least common multiple of steps for each dimension
    lcm = np.lcm.reduce(steps_all)
    print_res(day, 2, lcm)


if __name__ == '__main__':
    main()
