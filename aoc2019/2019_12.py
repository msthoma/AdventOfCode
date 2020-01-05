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
    # arrange dictionaries based on dimension
    positions = {k: {} for k in dimensions}
    velocities = {k: {} for k in dimensions}
    for i, dim in enumerate(positions.keys()):
        for j, moon in enumerate(moons):
            positions[dim][moon] = int(data[j][i])
            velocities[dim][moon] = 0

    # make copies of dictionaries
    pos1 = deepcopy(positions)
    vel1 = deepcopy(velocities)

    # simulate 1000 steps
    for _ in range(1000):
        for dim in dimensions:
            simulate(pos1[dim], vel1[dim])

    # calculate total energy
    total = 0
    for moon in moons:
        positional = 0
        kinetic = 0
        for dim in dimensions:
            positional += abs(pos1[dim][moon])
            kinetic += abs(vel1[dim][moon])
        total += positional * kinetic

    print_res(day, 1, total)

    # part 2
    # make copies to compare with original after each simulation
    pos2 = deepcopy(positions)
    vel2 = deepcopy(velocities)

    # simulate each dimension separately, until it reaches values identical to the original
    steps_all = []
    for dim in dimensions:
        steps = 0
        while True:
            simulate(pos2[dim], vel2[dim])
            steps += 1
            if positions[dim] == pos2[dim] and velocities[dim] == vel2[dim]:
                steps_all.append(steps)
                break

    # answer is the least common multiple of steps for each dimension
    lcm = np.lcm.reduce(steps_all)
    print_res(day, 2, lcm)


if __name__ == '__main__':
    main()
