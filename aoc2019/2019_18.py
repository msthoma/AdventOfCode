import itertools
import time
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

from utils.utils import get_script_file_name, input_fp, res_print

pts_tested = {}  # saves already tested positions to avoid re-calculations


def part_2_reachable(current_pt, grid, found_keys):
    keys = {}
    for quadrant, c_pt in enumerate(current_pt):
        for key, (pt, dist) in bfs_keys(c_pt, grid, found_keys).items():
            keys[key] = pt, dist, quadrant
    return keys


def shortest_path(current_pt, grid, found_keys):
    found_keys = "".join(sorted(found_keys))
    if (current_pt, found_keys) in pts_tested:
        return pts_tested[current_pt, found_keys]
    keys = bfs_keys(current_pt, grid, found_keys)
    if len(keys) == 0:  # no keys left, finished
        path_len = 0
    else:
        poss_paths = []
        for key, (pt, dist) in keys.items():
            poss_paths.append(dist + shortest_path(pt, grid, found_keys + key))
        path_len = min(poss_paths)
    pts_tested[current_pt, found_keys] = path_len
    return path_len


def shortest_path_p2(current_pts, grid, found_keys):
    found_keys = "".join(sorted(found_keys))
    if (current_pts, found_keys) in pts_tested:
        return pts_tested[current_pts, found_keys]
    keys = part_2_reachable(current_pts, grid, found_keys)
    if len(keys) == 0:  # no keys left, finished
        path_len = 0
    else:
        poss_paths = []
        for key, (pt, dist, quadrant) in keys.items():
            n_current_pts = tuple(pt if i == quadrant else p for i, p in enumerate(current_pts))
            poss_paths.append(dist + shortest_path_p2(n_current_pts, grid, found_keys + key))
        path_len = min(poss_paths)
    pts_tested[current_pts, found_keys] = path_len
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
    day = get_script_file_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

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

    # plt.show()

    # part 1
    time_start = time.time()
    pt_start = tuple(int(coord) for coord in np.where(grid_np == "@"))
    print("Calculating part 1 (takes anywhere between 1-2 min)...")
    res_print(day, 1, shortest_path(pt_start, grid, ""))
    print("Elapsed time: {:.2f}s".format(time.time() - time_start))

    # part 2
    # edit input as per part 2 instructions
    grid_np[39:42, 39:42] = [["@", "#", "@"],
                             ["#", "#", "#"],
                             ["@", "#", "@"]]
    # find starting positions
    starts_p2 = [s for s in np.where(grid_np == "@")]
    starts_p2 = tuple(i for i in zip(starts_p2[0], starts_p2[1]))

    # calculate part 2
    time_start = time.time()
    print("Calculating part 2 (takes anywhere between 4-5 min)...")
    res_print(day, 2, shortest_path_p2(starts_p2, grid_np.tolist(), ""))
    print("Elapsed time: {:.2f}s".format(time.time() - time_start))


if __name__ == '__main__':
    main()
