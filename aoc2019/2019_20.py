from collections import defaultdict, deque

from utils.utils import day_name, input_fp, print_res

in_key, out_key = "in", "out"


def find_min_path(start, end, grid, portals, recursive=False):
    """
    Finds minimum path length to end of maze, using breadth-first search
    """
    initial_layer = 0
    start, end = (start, initial_layer), (end, initial_layer)
    bfs = deque([start])
    visited = {start: 0}
    while bfs:
        pt = bfs.popleft()
        neighbours = get_neighbours(pt, grid, portals, recursive)
        for neighbour in neighbours:
            if neighbour == end:
                return visited[pt] + 1
            elif neighbour in visited:
                continue
            else:
                visited[neighbour] = visited[pt] + 1
                bfs.append(neighbour)


def get_neighbours(pt, grid, portals, recursive=False):
    """
    Determines reachable neighbours from given point
    Accounts for recursive layers of the maze, if they exist
    """
    current_pt, current_layer = pt
    neighbours = []
    # add neighbours via portals
    if current_pt in portals:
        portal_neighbour = [*portals[current_pt]][0]
        neighbour_layer = current_layer

        if recursive:  # case of multiple layers, for part 2
            direction = 1 if portals[current_pt][portal_neighbour] == in_key else -1
            if neighbour_layer + direction >= 0:
                # if neighbour_layer < 0 it's a portal on the "outest" layer, so  destination is not valid
                neighbours.append((portal_neighbour, neighbour_layer + direction))
        else:
            neighbours.append((portal_neighbour, neighbour_layer))

    # possible movements (diagonally is impossible)
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(4):
        y, x = current_pt[0] + dy[i], current_pt[1] + dx[i]
        if grid[y][x] == ".":  # append only path tiles
            neighbours.append(((y, x), current_layer))

    return neighbours


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip("\n")] for line in f.readlines()]

    # identify portals from input
    portal_pairs = defaultdict(dict)  # portal_pairs in form {"key": {(external pt): "out", (internal pt): "in"}}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].isalpha():
                if i + 2 < len(grid):  # v down
                    if grid[i + 1][j].isalpha() and grid[i + 2][j] == ".":
                        key, pt = grid[i][j] + grid[i + 1][j], (i + 2, j)
                        if pt[0] == 2:  # outer top
                            portal_pairs[key][pt] = out_key
                        else:  # inner down
                            portal_pairs[key][pt] = in_key

                if i - 2 >= 0:  # v up
                    if grid[i - 1][j].isalpha() and grid[i - 2][j] == ".":
                        key, pt = grid[i - 1][j] + grid[i][j], (i - 2, j)
                        if pt[0] == 28:  # inner top
                            portal_pairs[key][pt] = in_key
                        else:  # outer down
                            portal_pairs[key][pt] = out_key

                if j + 2 < len(grid[0]):  # h right
                    if grid[i][j + 1].isalpha() and grid[i][j + 2] == ".":
                        key, pt = grid[i][j] + grid[i][j + 1], (i, j + 2)
                        if pt[1] == 2:  # outer left
                            portal_pairs[key][pt] = out_key
                        else:  # inner right
                            portal_pairs[key][pt] = in_key

                if j - 2 >= 0:  # v left
                    if grid[i][j - 1].isalpha() and grid[i][j - 2] == ".":
                        key, pt = grid[i][j - 1] + grid[i][j], (i, j - 2)
                        if pt[1] == 28:  # inner left
                            portal_pairs[key][pt] = in_key
                        else:  # outer right
                            portal_pairs[key][pt] = out_key

    portals = {}
    for k, v in portal_pairs.items():
        if len(v) == 2:
            p1, p2 = v.keys()
            dir1, dir2 = v.values()
            portals[p1], portals[p2] = {p2: dir1}, {p1: dir2}

    start, end = [*portal_pairs["AA"]][0], [*portal_pairs["ZZ"]][0]

    # part 1
    print_res(day, 1, find_min_path(start, end, grid, portals))

    # part 2
    print_res(day, 2, find_min_path(start, end, grid, portals, recursive=True))


if __name__ == '__main__':
    main()
