import numpy as np

from utils.utils import res_print2, get_data

if __name__ == '__main__':
    data = [[list(map(int, point.split(","))) for point in line.split(" -> ")] for line in get_data().splitlines()]

    h_or_v_only = list(filter(lambda l: l[0][0] == l[1][0] or l[0][1] == l[1][1], data))
    diag_only = list(filter(lambda l: l[0][0] != l[1][0] and l[0][1] != l[1][1], data))

    max_x, max_y = max([max([p[0] for p in line]) for line in data]), max([max([p[1] for p in line]) for line in data])

    grid = np.zeros((max_x + 10, max_y + 10), dtype=int)

    for line in h_or_v_only:
        x_0, x_1 = sorted([line[0][1], line[1][1]])
        y_0, y_1 = sorted([line[0][0], line[1][0]])
        x_1 += 1
        y_1 += 1
        grid[np.arange(x_0, x_1) if x_1 > x_0 else np.array([x_0] * (y_1 - y_0)),
             np.arange(y_0, y_1) if y_1 > y_0 else np.array([y_0] * (x_1 - x_0))] += 1

    res_print2(np.sum(grid >= 2), 1)

    for line in diag_only:
        x_0, x_1 = line[0][1], line[1][1]
        x_sort = x_0 > x_1
        x_0, x_1 = sorted([x_0, x_1])
        x_1 += 1
        y_0, y_1 = line[0][0], line[1][0]
        y_sort = y_0 > y_1
        y_0, y_1 = sorted([y_0, y_1])
        y_1 += 1

        grid[np.arange(x_0, x_1) if not x_sort else np.flip(np.arange(x_0, x_1)),
             np.arange(y_0, y_1) if not y_sort else np.flip(np.arange(y_0, y_1))] += 1

    res_print2(np.sum(grid >= 2), 2)
