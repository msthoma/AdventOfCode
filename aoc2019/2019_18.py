import itertools

import matplotlib.pyplot as plt
import numpy as np

from utils.utils import day_name, input_fp


def get_neighbours(point, grid):
    """
    Determines reachable neighbours from given point
    """
    # possible movements, diagonally impossible
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


def paths(graph, start, end):
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])


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
    plt.annotate(robot, (40, 40))
    for dk in doors_keys:
        plt.annotate(dk, xy=np.where(grid_np == dk), ha='center', va='center', size=7,
                     bbox=door_bbox if dk.isupper() else key_bbox)
    # plt.savefig(f"{day}_maze.svg")
    plt.show()
    print(robot)
    # part 2

    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['C'],
    #          'E': ['F'],
    #          'F': ['C']}
    #
    # for path in paths(graph, 'A', 'D'):
    #     print(path)

    print(get_neighbours((1, 2), grid))
    print(data_int.shape)


if __name__ == '__main__':
    main()
