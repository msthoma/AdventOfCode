from utils.utils import day_name, input_fp, print_res


def biodiversity(grid):
    score = 0
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if tile == "#":
                score += 2 ** (i * len(row) + j)
    return score


def sim_turn(grid):
    next_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            tile_type = grid[i][j]
            count = count_adjacent(grid, (i, j))
            if tile_type == "#" and count == 1:
                row.append("#")
            elif tile_type == "." and count in [1, 2]:
                row.append("#")
            else:
                row.append(".")
        next_grid.append("".join(row))
    return next_grid


def sim_turn_rec(grids, recursive=False):
    next_grid = []
    for i in range(len(grids)):
        row = []
        for j in range(len(grids[0])):
            tile_type = grids[i][j]
            count = count_adjacent(grids, (i, j))
            if tile_type == "#" and count == 1:
                row.append("#")
            elif tile_type == "." and count in [1, 2]:
                row.append("#")
            else:
                row.append(".")
        next_grid.append("".join(row))
    return next_grid


def count_adjacent(grid, tile):
    count = 0
    for i, j in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        i, j = i + tile[0], j + tile[1]
        if i >= 0 and j >= 0:
            try:
                if grid[i][j] == "#":
                    count += 1
            except IndexError:
                pass
    return count


def count_adjacent_rec(grid, tile, recursive=False, level=0):
    count = 0
    for i, j in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        i, j = i + tile[0], j + tile[1]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
            # up or down, left or right, layer is one level up
            level -= 1
        if (i, j) == (2, 2):
            # nested layer, one level down
            level_down = level + 1
            if tile == (1, 2):  # top
                slice
                pass
            elif tile == (3, 2):  # bottom
                pass
            elif tile == (2, 1):  # left
                pass
            elif tile == (2, 3):  # right
                pass
        else:
            # same level
            if grid[i][j] == "#":
                count += 1

    return count


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [line.strip() for line in f.readlines()]

    # part 1
    grid_1 = grid.copy()
    # loop until first repeating grid pattern occurs
    layouts = []
    while True:
        grid_1 = sim_turn(grid_1)
        layout = "".join(grid_1)
        if layout in layouts:
            break
        layouts.append(layout)
    # calculate biodiversity
    print_res(day, 1, biodiversity(grid_1))

    # part 2
    # create dictionary to hold recursive grids and populate it with empty grids, and the original grid at 0
    empty_grid = ["".join(["."] * 5) for _ in range(5)]
    recursive_grids = {i: empty_grid.copy() for i in range(-100, 101)}
    recursive_grids[0] = grid.copy()

    print(recursive_grids)


if __name__ == '__main__':
    main()
