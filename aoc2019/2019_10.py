import math

import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter

from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()
    asteroid_map = np.array([[1 if s == "#" else 0 for s in line.strip()] for line in input_data])

    asteroid_coords = []

    for x in range(asteroid_map.shape[0]):
        for y in range(asteroid_map.shape[1]):
            if asteroid_map[x, y] == 1:
                asteroid_coords.append([x, y])

    # part 1
    los_asteroid_counts = {}
    los_asteroids_rel = {}

    for station in asteroid_coords:
        in_los = set()

        for asteroid in asteroid_coords:
            if asteroid != station:
                dx, dy = np.array(asteroid) - np.array(station)
                gcd = abs(math.gcd(dx, dy))
                in_los.add((dx // gcd, dy // gcd))

        los_asteroids_rel[tuple(station)] = in_los
        los_asteroid_counts[tuple(station)] = len(in_los)

    station = max(los_asteroid_counts, key=los_asteroid_counts.get)

    print_res(day, 1, los_asteroid_counts[station])

    # part 2
    los_angles = {math.atan2(y, x): (x, y) for x, y in los_asteroids_rel[station]}
    print(los_angles)
    test = sorted(los_angles.values(), reverse=True)
    los_destroyed_order = sorted(los_angles.keys(), reverse=True)
    order = np.array([station + np.array(los_angles[k]) for k in sorted(los_angles.keys(), reverse=True)])
    print(len(asteroid_coords), len(order))

    asteroid_200th = los_angles[los_destroyed_order[200 - 1]]
    dx, dy = asteroid_200th

    x, y = station[0] + dx, station[1] + dy

    while [x, y] not in asteroid_coords:
        x, y = x + dx, y + dy

    print_res(day, 2, y * 100 + x)

    # part 2 asteroid destruction animation
    asteroid_coords = np.array(asteroid_coords)

    fig = plt.figure()
    ax = plt.axes(xlim=(-2, 34), ylim=(34, -2), aspect="equal")
    ax.xaxis.tick_top()
    sct = ax.scatter([], [], s=15)
    annotation = ax.annotate("",
                             xy=station, xycoords='data',
                             xytext=station, textcoords='data',
                             arrowprops=dict(arrowstyle="-",
                                             edgecolor="red",
                                             connectionstyle="arc3"),
                             )
    annotation.set_animated(True)

    def init():
        return sct, annotation

    def update(i):
        # mask destroyed from coords
        destroyed_mask = np.ones(len(order), dtype=bool)
        destroyed_mask[np.arange(i)] = False
        # plot again
        sct.set_offsets(order[destroyed_mask])
        annotation.xy = order[i]
        # annotation.xytext = station
        # annotation = ax.annotate("",
        #                           xy=order[i], xycoords='data',
        #                           xytext=station, textcoords='data',
        #                           arrowprops=dict(arrowstyle="-",
        #                                           edgecolor="red",
        #                                           connectionstyle="arc3"),
        #                           )
        return sct, annotation

    anim = animation.FuncAnimation(fig, update, frames=20, init_func=init, interval=200, blit=True)
    # writer = FFMpegWriter(fps=10, bitrate=1800)
    anim.save('basic_animation.mp4', writer="imagemagick")
    plt.show()


if __name__ == '__main__':
    main()
