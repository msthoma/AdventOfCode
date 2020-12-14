import math

from utils.utils import get_data, res_print2


def move(instr: list, pos: tuple, direction: str):
    dirs, moves = "NESW", [[0, 1], [1, 0], [0, -1], [-1, 0]]
    move_dict = {d: m for d, m in zip(dirs, moves)}

    if instr[0] == "L":
        direction = dirs[dirs.index(direction) - instr[1] // 90]
    elif instr[0] == "R":
        direction = dirs[(dirs.index(direction) + instr[1] // 90) % len(dirs)]
    else:
        dir_to_move = direction if instr[0] == "F" else instr[0]
        assert dir_to_move in dirs
        pos = tuple(map(lambda m: m[0] + instr[1] * m[1],
                        zip(pos, move_dict[dir_to_move])))

    return pos, direction


def move_by_waypoint(instr: list, pos: tuple, waypoint: tuple):
    if instr[0] == "F":
        pos = tuple(map(lambda m: m[0] + instr[1] * m[1], zip(pos, waypoint)))
    elif instr[0] in "NESW":
        waypoint, _ = move(instr, waypoint, instr[0])
    elif instr[0] in "RL":
        x, y = waypoint
        rad = math.radians(instr[1])
        xx, yy = 0, 0
        # rotate by angle around origin, see
        # https://en.wikipedia.org/wiki/Rotation_matrix
        if instr[0] == "R":
            # rotate clockwise
            xx = x * math.cos(rad) + y * math.sin(rad)
            yy = -x * math.sin(rad) + y * math.cos(rad)
        elif instr[0] == "L":
            # rotate counter-clockwise
            xx = x * math.cos(rad) - y * math.sin(rad)
            yy = x * math.sin(rad) + y * math.cos(rad)
        waypoint = (round(xx), round(yy))
    return pos, waypoint


def main():
    # use right-handed Cartesian coordinate system in this case, with the
    # x-axis to the right and the y-axis up
    data = [[i[0], int(i[1:])] for i in get_data().splitlines()]
    for i in data:
        if i[0] in "LR":
            assert i[1] in [90, 180, 270]

    # part a
    pos_a, direction = (0, 0), "E"

    # part b
    pos_b, waypoint = (0, 0), (10, 1)

    for instr in data:
        pos_a, direction = move(instr, pos_a, direction)
        pos_b, waypoint = move_by_waypoint(instr, pos_b, waypoint)

    res_print2(sum(map(abs, pos_a)), 1)
    res_print2(sum(map(abs, pos_b)), 2)


if __name__ == '__main__':
    main()
