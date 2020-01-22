import numpy as np
from collections import defaultdict
from utils.utils import day_name, input_fp


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip("\n")] for line in f.readlines()]

    # part 1
    grid_np = np.array(grid)
    print(grid_np[:, 37])
    portals = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].isalpha():
                if i + 2 < len(grid):  # v down
                    if grid[i + 1][j].isalpha() and grid[i + 2][j] == ".":
                        portals[grid[i][j] + grid[i + 1][j]].append((i + 2, j))

                if i - 2 >= 0:  # v up
                    if grid[i - 1][j].isalpha() and grid[i - 2][j] == ".":
                        portals[grid[i - 1][j] + grid[i][j]].append((i - 2, j))

                if j + 2 < len(grid[0]):  # h right
                    if grid[i][j + 1].isalpha() and grid[i][j + 2] == ".":
                        portals[grid[i][j] + grid[i][j + 1]].append((i, j + 2))

                if j - 2 >= 0:  # v left
                    if grid[i][j - 1].isalpha() and grid[i][j - 2] == ".":
                        portals[grid[i][j - 1] + grid[i][j]].append((i, j - 2))

    for k, v in portals.items():
        print(k, v)

    # part 2


if __name__ == '__main__':
    main()
