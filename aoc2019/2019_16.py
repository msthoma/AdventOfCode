import time

from tqdm import tqdm

from utils.utils import day_name, input_fp, print_res


def get_pattern(i, leng):
    base_pat = [0, 1, 0, -1]
    pat, j = [], 0
    while len(pat) <= leng:
        pat.extend([base_pat[j % len(base_pat)]] * i)
        j += 1
    return pat[1:leng + 1]


def run_fft(signal, times):
    leng = len(signal)
    for _ in range(times):
        temp_data = []
        for i in range(1, leng + 1):
            pat = get_pattern(i, leng)
            temp_data.append(abs(sum(si * pv for si, pv in zip(signal, pat))) % 10)
        signal = temp_data
    return signal


def main():
    start = time.time()

    day = day_name()

    with open(input_fp(day), "r") as f:
        data = [int(i) for i in f.read().strip()]

    # part 1
    print_res(day, 1, "".join(str(i) for i in run_fft(data.copy(), 100)[:8]))

    # part 2
    # data = [int(i) for i in "03036732577212944063491565474664"]
    offset = int("".join(str(i) for i in data[:7]))
    data_2 = data * 10000
    data_2 = data_2[offset:]  # pattern until offset will be all zeros, so can be ignored
    leng = len(data_2)

    for _ in range(100):
        temp_data = []
        t = tqdm(total=leng)
        for i in range(0, leng):
            temp_data.append(sum(data_2[i:]) % 10)
            t.update()
        data_2 = temp_data
        t.close()

    print_res(day, 2, "".join(str(i) for i in data_2[:8]))

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
