from tqdm import tqdm

from utils.utils import get_data, res_print2


def calculate(data, xth_num):
    t = tqdm(total=xth_num)
    t.update(len(data))
    prev, indices = data[-1], {num: i + 1 for i, num in enumerate(data)}
    for i in range(len(data), xth_num):
        indices[prev], prev = i, i - indices[prev] if prev in indices else 0
        t.update()
    t.close()
    return prev


def main():
    data = [int(i) for i in get_data().split(",")]

    res_print2(calculate(data, 2020), 1)
    res_print2(calculate(data, 30000000), 2)


if __name__ == '__main__':
    main()
