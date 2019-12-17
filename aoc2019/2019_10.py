import numpy as np

from utils.utils import day_name, input_fp


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()
    asteroid_map = np.array([[1 if s == "#" else 0 for s in line.strip()] for line in input_data])

    # numpy option to print arrays entirely
    np.set_printoptions(threshold=np.inf)

    print(asteroid_map.shape)

    asteroid_coord = []

    for y in range(asteroid_map.shape[0]):
        for x in range(asteroid_map.shape[1]):
            if asteroid_map[y, x] == 1:
                asteroid_coord.append([x, y])

    for x, y in asteroid_coord:
        if asteroid_map[y, x] != 1:
            print(x, y)

    print(np.linalg.norm(np.array(asteroid_coord[0]) - np.array(asteroid_coord[2])))
    print(len(asteroid_coord))
    for a in asteroid_coord[:1]:
        # euclidean
        a_eucl = {}
        for b in asteroid_coord:
            if a == b:
                continue
            a_eucl[tuple(b)] = np.linalg.norm(np.array(a) - np.array(b))
        print(len(a_eucl))


if __name__ == '__main__':
    main()
