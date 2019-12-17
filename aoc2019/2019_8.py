from utils.utils import day_name, input_fp, print_res
import numpy as np


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        img = np.array([int(i) for i in f.read().strip()])

    img_reshaped = np.split(img.reshape((-1, 25)), len(img) / (6 * 25))
    zero_counts = [np.count_nonzero(s == 0) for s in img_reshaped]
    min_zeros_layer = img_reshaped[zero_counts.index(min(zero_counts))]

    print_res(day, 1, np.count_nonzero(min_zeros_layer == 1) * np.count_nonzero(min_zeros_layer == 2))


if __name__ == '__main__':
    main()
