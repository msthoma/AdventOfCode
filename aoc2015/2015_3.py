from utils.utils import get_data, res_print2


def calc_new_pos(start_pos: tuple, move: str):
    y, x = start_pos
    if move == ">":
        x += 1
    elif move == "<":
        x -= 1
    elif move == "^":
        y += 1
    elif move == "v":
        y -= 1
    else:
        raise ValueError
    return y, x


def main():
    data = get_data()

    path_a = [(0, 0)]  # (y, x)
    for move in data:
        path_a.append(calc_new_pos(path_a[-1], move))

    res_print2(len(set(path_a)), 1)

    path_santa, path_robot = [(0, 0)], [(0, 0)]
    paths_b = [path_santa, path_robot]
    for i, move in enumerate(data):
        paths_b[i % 2].append(calc_new_pos(paths_b[i % 2][-1], move))

    res_print2(len(set(path_santa + path_robot)), 2)


if __name__ == '__main__':
    main()
