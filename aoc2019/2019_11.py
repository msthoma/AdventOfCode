from aoc2019.intcode import computer
from utils.utils import get_script_file_name, input_fp, res_print
from collections import defaultdict

d_list = list("LURD")
d_dict = {k: v for k, v in zip(d_list, range(4))}


def turn(position, direction, instruction):
    x, y = position

    if instruction == 0:
        instruction = -1

    new_dir = d_list[(d_dict[direction] + instruction) % len(d_list)]

    if new_dir == "L":
        x -= 1
    elif new_dir == "U":
        y += 1
    elif new_dir == "R":
        x += 1
    elif new_dir == "D":
        y -= 1

    return (x, y), new_dir


def run_robot(intcode, start_color=0):
    robot_path = [(0, 0)]
    robot_direction = ["U"]
    panel_colors = defaultdict(int)

    if start_color == 1:
        panel_colors[robot_path[-1]] = 1

    ip = 0
    while True:
        current_panel = robot_path[-1]
        current_color = panel_colors[current_panel]
        # get color
        res = computer(intcode, [current_color], ip=ip, feedback=True, extend=True)

        # check if finished
        halt = res["halt"]
        if halt:
            break

        # paint panel with color
        panel_colors[robot_path[-1]] = res["output"][0]

        # update ip
        ip = res["ip"]

        if start_color == 1:
            panel_colors[robot_path[-1]] = 0

        # get instruction
        res = computer(intcode, [current_color], ip=ip, feedback=True)
        instruction = res["output"][0]

        # update ip
        ip = res["ip"]

        new_pos, new_dir = turn(current_panel, robot_direction[-1], instruction)

        robot_path.append(new_pos)
        robot_direction.append(new_dir)

    return panel_colors, robot_path


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    robot_path = run_robot(intcode.copy(), start_color=1)[1]

    res_print(day, 1, len(set(robot_path)))


if __name__ == '__main__':
    main()
