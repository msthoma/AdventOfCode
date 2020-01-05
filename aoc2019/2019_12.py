from utils.utils import day_name, input_fp
import re


def main():
    day = day_name()

    pattern = r"<x=(-?\d+).+y=(-?\d+).+z=(-?\d+)>"

    with open(input_fp(day), "r") as f:
        data = [re.match(pattern, line).groups() for line in f.readlines()]

    moons = {}

    for [x, y, z], moon in zip(data, ["Io", "Europa", "Ganymede", "Callisto"]):
        moons[moon] = {"x": x, "y": y, "z": z}
        print(moons[moon])


if __name__ == '__main__':
    main()
