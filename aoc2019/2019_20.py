from collections import defaultdict, deque

from utils.utils import day_name, input_fp, print_res


def get_neighbours(point, grid, portals):
    """
    Determines reachable neighbours from given point
    """
    neighbours = []
    # add neighbours via portals
    if point in portals:
        neighbours.append(portals[point])

    # possible movements (diagonally is impossible)
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(4):
        y, x = point[0] + dy[i], point[1] + dx[i]
        if grid[y][x] == ".":  # append only path tiles
            neighbours.append((y, x))

    return neighbours


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        grid = [[c for c in line.strip("\n")] for line in f.readlines()]

    # part 1
    portal_pairs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].isalpha():
                if i + 2 < len(grid):  # v down
                    if grid[i + 1][j].isalpha() and grid[i + 2][j] == ".":
                        portal_pairs[grid[i][j] + grid[i + 1][j]].append((i + 2, j))

                if i - 2 >= 0:  # v up
                    if grid[i - 1][j].isalpha() and grid[i - 2][j] == ".":
                        portal_pairs[grid[i - 1][j] + grid[i][j]].append((i - 2, j))

                if j + 2 < len(grid[0]):  # h right
                    if grid[i][j + 1].isalpha() and grid[i][j + 2] == ".":
                        portal_pairs[grid[i][j] + grid[i][j + 1]].append((i, j + 2))

                if j - 2 >= 0:  # v left
                    if grid[i][j - 1].isalpha() and grid[i][j - 2] == ".":
                        portal_pairs[grid[i][j - 1] + grid[i][j]].append((i, j - 2))
    portals = {}
    for k, v in portal_pairs.items():
        if len(v) == 2:
            p1, p2 = v
            portals[p1], portals[p2] = p2, p1

    start, end = portal_pairs["AA"][0], portal_pairs["ZZ"][0]
    bfs = deque([start])
    visited = {start: 0}
    answered = False
    while bfs:
        pt = bfs.popleft()
        neighbours = get_neighbours(pt, grid, portals)
        for neighbour in neighbours:
            if neighbour == end:
                print_res(day, 1, visited[pt] + 1)
                answered = True
            elif neighbour in visited:
                continue
            else:
                visited[neighbour] = visited[pt] + 1
                bfs.append(neighbour)
        if answered:
            break

    # part 2


if __name__ == '__main__':
    main()
