from collections import defaultdict

from utils import utils


def checksum(orbits):
    d_orbits = defaultdict(list)
    pass


def main():
    day = utils.get_day_name()
    with open(f"{day}.txt", "r") as f:
        input_data = f.read().splitlines()

    print(input_data)


if __name__ == '__main__':
    main()
