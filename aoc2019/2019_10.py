import math

import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

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

    los_destroyed_order = np.array([station + np.array(los_angles[k]) for k in sorted(los_angles.keys(), reverse=True)])

    asteroid_200th = los_angles[sorted(los_angles.keys(), reverse=True)[200 - 1]]
    dx, dy = asteroid_200th

    x, y = station[0] + dx, station[1] + dy

    while [x, y] not in asteroid_coords:
        x, y = x + dx, y + dy

    print_res(day, 2, y * 100 + x)

    # part 2 asteroid destruction animation
    n_frames = 200
    asteroid_coords = np.array(asteroid_coords)

    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes(xlim=(-3, 35), ylim=(35, -3), aspect="equal")
    ax.xaxis.tick_top()
    sct = ax.scatter([], [], s=15)
    title = ax.text(0.5, 0.02, "", transform=ax.transAxes, ha="center")
    annotation = ax.annotate("",
                             xy=station, xycoords='data',
                             xytext=station, textcoords='data',
                             arrowprops=dict(arrowstyle="-",
                                             edgecolor="red",
                                             connectionstyle="arc3"),
                             )
    annotation.set_animated(True)

    def init():
        return sct, annotation, title

    def update(i):
        # mask destroyed asteroid coords so far
        destroyed = los_destroyed_order[:i, ]
        destroyed_mask = np.ones(len(asteroid_coords), dtype=bool)
        # https://stackoverflow.com/a/38674038 "Find the row indexes of several values in a numpy array"
        destroyed_mask[np.where((asteroid_coords == destroyed[:, None]).all(-1))[1]] = False

        # replace scatter with remaining asteroids and new laser beam
        sct.set_offsets(asteroid_coords[destroyed_mask])
        if i == n_frames - 1:
            title.set_text(f"ANSWER: {n_frames}th asteroid at {los_destroyed_order[i]}")
        else:
            title.set_text(f"Step {i + 1}: Destroying asteroid at {los_destroyed_order[i]}")
        annotation.xy = los_destroyed_order[i]
        return sct, annotation, title

    def save_progress(i, n):
        print(f'\rSaving to gif... (frame {i} of {n})', end="")

    anim = animation.FuncAnimation(fig, update,
                                   init_func=init, frames=n_frames,
                                   interval=200, repeat_delay=3000, blit=True)

    anim.save(f"{day}_animation.gif", writer="imagemagick", progress_callback=save_progress)
    plt.show()


if __name__ == '__main__':
    main()
