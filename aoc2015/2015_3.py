import re

from utils import utils


def main():
    day = utils.day_name()
    with open(f"{day}.txt", "r") as f:
        input_data = f.read()
    print(len(input_data))

    houses = [[0, 0]]
    for i, move in enumerate(input_data):
        previous_pos = houses[i]


if __name__ == '__main__':
    main()
