import re
from itertools import combinations

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


if __name__ == '__main__':
    main()
