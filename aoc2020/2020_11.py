import copy
import sys
from itertools import combinations

import numpy as np

from utils.utils import get_data, res_print2


def get_neighbours(point: tuple, grid: np.array, line_of_sight: bool = False):
    """ los = line of sight """
    row_r, col_r = range(grid.shape[0]), range(grid.shape[1])

    directions = set(combinations([0, 1, -1, 0, 1, -1], 2))
    directions.remove((0, 0))
    directions = sorted(directions)

    # 0 1 2
    # 3 x 4
    # 5 6 7

    neighbours = []
    for y, x in directions:
        row, col = point
        while True:
            row, col = row + y, col + x
            if row in row_r and col in col_r:
                if grid[row, col] == "#" or grid[row, col] == "L":
                    neighbours.append((row, col))
                    break
                elif line_of_sight:
                    # continue until a neighbour is found in this direction
                    continue
                else:
                    break
            else:
                break
    return neighbours


def next_round(layout: np.array, thresh: int, los: bool = False):
    """ los = line of sight """
    new_layout = copy.deepcopy(layout)

    row_r, col_r = range(layout.shape[0]), range(layout.shape[1])

    for row in row_r:
        for col in col_r:
            n_occ_neighbours = 0
            for neighbour in get_neighbours((row, col), layout, los):
                if layout[neighbour] == "#":
                    n_occ_neighbours += 1
            if layout[row, col] == "L" and n_occ_neighbours == 0:
                new_layout[row, col] = "#"
            elif layout[row, col] == "#" and n_occ_neighbours >= thresh:
                new_layout[row, col] = "L"
    return copy.deepcopy(new_layout)


def main():
    np.set_printoptions(threshold=sys.maxsize)
    data = np.array([list(l) for l in get_data().splitlines()])
    # data_tuple = tuple(tuple(l) for l in get_data().splitlines())

    # part a
    layout1 = copy.deepcopy(data)
    while True:
        new_layout = next_round(layout1, thresh=4, los=False)
        if np.array_equal(layout1, new_layout):
            break
        layout1 = copy.deepcopy(new_layout)

    # part b
    layout2 = copy.deepcopy(data)
    while True:
        new_layout = next_round(layout2, thresh=5, los=True)
        if np.array_equal(layout2, new_layout):
            break
        layout2 = copy.deepcopy(new_layout)

    res_print2((layout1 == "#").sum(), 1)
    res_print2((layout2 == "#").sum(), 2)


if __name__ == '__main__':
    main()
