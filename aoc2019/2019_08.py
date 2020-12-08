import matplotlib.pyplot as plt
import numpy as np

from utils.utils import get_script_file_name, input_fp, res_print


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        img = np.array([int(i) for i in f.read().strip()])

    # img dimensions
    height = 6
    width = 25

    # part 1
    img_reshaped = np.split(img.reshape((-1, width)), len(img) / (height * width))
    zero_counts = [np.count_nonzero(s == 0) for s in img_reshaped]
    min_zeros_layer = img_reshaped[zero_counts.index(min(zero_counts))]

    res_print(day, 1, np.count_nonzero(min_zeros_layer == 1) * np.count_nonzero(min_zeros_layer == 2))

    # numpy option to print arrays entirely
    np.set_printoptions(threshold=np.inf)

    # part 2
    img_reshaped = np.stack(img_reshaped, axis=2)

    res = []
    for i in range(height):
        for j in range(width):
            for v in img_reshaped[i, j, :]:
                if v in [0, 1]:
                    res.append(v)
                    break

    res = np.reshape(res, (height, width))
    res_print(day, 2, res)

    # plot image
    plt.figure(figsize=(4, 1.5))
    plt.imshow(res, cmap="binary")
    plt.title("Part 2 decoded image")
    plt.savefig("2019_8_2_img.svg")
    # plt.show()


if __name__ == '__main__':
    main()
