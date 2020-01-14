import numpy as np
import time

from utils.utils import day_name, input_fp, print_res


def get_pattern(i, leng):
    base_pat = [0, 1, 0, -1]
    pat, j = [], 0
    while len(pat) <= leng:
        pat.extend([base_pat[j % len(base_pat)]] * i)
        j += 1
    return pat[1:leng + 1]


def run_fft(signal, times):
    leng = signal.size
    for _ in range(times):
        temp_data = []
        for i in range(1, leng + 1):
            pat = np.array(get_pattern(i, leng))
            temp_data.append(abs(np.sum(signal * pat)) % 10)
        signal = np.array(temp_data)
    return signal


def main():
    start = time.time()

    day = day_name()

    with open(input_fp(day), "r") as f:
        data = [int(i) for i in f.read().strip()]

    # part 1
    data_1 = data.copy()
    leng = len(data_1)
    for _ in range(100):
        temp_data = []
        for i in range(1, leng + 1):
            pat = get_pattern(i, leng)
            temp_data.append(abs(sum(si * pv for si, pv in zip(data_1, pat))) % 10)
        data_1 = temp_data

    print_res(day, 1, "".join(str(i) for i in data_1[:8]))

    # part 1 try with numpy
    with open(input_fp(day), "r") as f:
        data_np = np.array([int(i) for i in f.read().strip()])
    print_res(day, 1, "".join(str(i) for i in run_fft(data_np.copy(), 100)[:8]))

    # data_11 = np.array(data)

    # part 2
    # offset = "".join(str(i) for i in data[:7])
    # data_2 = data * 10000
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
