import itertools
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

from utils.utils import day_name, input_fp, print_res

pts_tested = {}  # saves already tested positions to avoid re-calculations


def shortest_path(current_pt, grid, found_keys):
    hk = "".join(sorted(found_keys))
    if (current_pt, hk) in pts_tested:
        return pts_tested[current_pt, hk]
    keys = bfs_keys(current_pt, grid, found_keys)
    if len(keys) == 0:  # no keys left, finished
        path_len = 0
    else:
        poss_paths = []
        for key, (pt, dist) in keys.items():
            # print(key, pt, dist)
            # hk.append(key)
            poss_paths.append(dist + shortest_path(pt, grid, hk + key))
        path_len = min(poss_paths)
    pts_tested[current_pt, hk] = path_len
    return path_len


def bfs_keys(current_pt, grid, found_keys):
    """
    Performs breadth-first search, to find all reachable keys and their distance from current position
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

            point_type = grid[ngbr[0]][ngbr[1]]

            if point_type.isupper() and point_type.lower() not in found_keys:  # door and do not have key
                continue
            elif point_type.islower() and point_type not in found_keys:  # found key
                keys[point_type] = ngbr, pt_distances[ngbr]
            else:
                bfs.append(ngbr)
    return keys


def get_neighbours(point, grid):
    """
    Determines reachable neighbours from given point
    """
    # possible movements (diagonally is impossible)
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    neighbours = []
    for i in range(4):
        y, x = point[0] + dy[i], point[1] + dx[i]

        # skip if not within maze's bounds (NOT actually needed since there is a "#" barrier around the maze)
        # if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        #     continue

        point_type = grid[y][x]
        if point_type == "#":  # skip if wall
            continue
        neighbours.append((y, x))

    return neighbours


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

    # part 1
    print_res(day, 1, shortest_path((40, 40), grid, ""))

    # part 2

    # animation
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
        y, x = np.where(grid_np == dk)
        plt.annotate(dk, xy=(x, y), ha='center', va='center', size=7,
                     bbox=door_bbox if dk.isupper() else key_bbox)
    # plt.savefig(f"{day}_maze.pdf")

    plt.show()


if __name__ == '__main__':
    main()
