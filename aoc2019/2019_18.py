import itertools
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

from utils.utils import day_name, input_fp


def shortest_path(current_pt, grid, havekeys):
    pass


def bfs_keys(current_pt, grid, havekeys):
    """
    Determines reachable keys from current position
    """
    keys = {}
    pt_distances = {current_pt: 0}
    bfs = deque([current_pt])

    while bfs:
        new_pt = bfs.popleft()

        for ngbr in get_neighbours(new_pt, grid):
            if ngbr in pt_distances:  # already visited this point
                continue

            pt_distances[ngbr] = pt_distances[new_pt] + 1

            point_type = grid[new_pt[0]][new_pt[1]]
            if point_type not in [".", "@"]:
                if point_type.isupper() and point_type.lower() not in havekeys:  # door and do not have key
                    continue
                elif point_type.islower() and point_type not in havekeys:  # found key
                    keys[point_type] = ngbr, pt_distances[ngbr]
            else:
                bfs.append(ngbr)
    return keys


def get_neighbours(point, grid):
    """
    Determines reachable neighbours from given point
    """
    # possible movements, diagonally is impossible
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    neighbours = []
    for i in range(4):
        x, y = point[0] + dx[i], point[1] + dy[i]
        if not (0 <= x <= len(grid) and 0 <= y <= len(grid[0])):  # skip if not within maze's bounds
            continue
        point_type = grid[x][y]
        if point_type == "#":  # skip if wall
            continue
        neighbours.append((x, y))

    return neighbours


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

    # part 1
    unique = set(itertools.chain.from_iterable(grid))
    unique -= {'#', '.', '@'}
    doors_keys = sorted(unique)
    doors = [x for x in doors_keys if x.isupper()]
    keys = [x for x in doors_keys if x.islower()]

    grid_np = np.array(grid)
    data_int = grid_np.copy()
    data_int[data_int == "#"] = 0
    data_int[data_int != "0"] = 1
    data_int = data_int.astype(int)

    robot = u"\U0001F916"
    plt.figure(figsize=(20, 20))
    plt.imshow(data_int, cmap='gray')
    door_bbox = dict(boxstyle="square,pad=0.2", fc="chocolate", ec="saddlebrown", lw=1)
    key_bbox = dict(boxstyle="circle,pad=0.2", fc="yellow", ec="gold", lw=1)
    plt.annotate("@", np.where(grid_np == "@"))
    for dk in doors_keys:
        if dk == "R":
            print(np.where(grid_np == dk))
        plt.annotate(dk, xy=np.where(grid_np == dk), ha='center', va='center', size=7,
                     bbox=door_bbox if dk.isupper() else key_bbox)
    # plt.savefig(f"{day}_maze.pdf")

    print(bfs_keys((40, 40), grid, ""))
    # plt.show()

    # part 2


if __name__ == '__main__':
    main()
