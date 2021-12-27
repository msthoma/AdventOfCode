import time

import numpy as np

from utils.utils import res_print2, get_data

if __name__ == '__main__':
    data = np.array([list(map(int, line.strip())) for line in get_data().splitlines()])

    start = time.time()
    risk_of_low_points = 0
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            point, neighbours = data[i, j], []
            for p in range(len(dy)):
                y, x = i + dy[p], j + dx[p]
                if 0 <= y < data.shape[0] and 0 <= x < data.shape[1]:
                    neighbours.append(data[y, x])

            if len(neighbours) != 0 and all(point < n for n in neighbours):
                risk_of_low_points += point + 1

    res_print2(risk_of_low_points, 1, start)
