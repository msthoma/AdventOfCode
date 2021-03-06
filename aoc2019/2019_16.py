from tqdm import tqdm

from utils.utils import get_script_file_name, input_fp, res_print


def get_pattern(i, leng):
    base_pat = [0, 1, 0, -1]
    pat, j = [], 0
    while len(pat) <= leng:
        pat.extend([base_pat[j % len(base_pat)]] * i)
        j += 1
    return pat[1:leng + 1]


def run_fft(signal, times):
    leng = len(signal)
    t = tqdm(total=times)
    t.set_description("Calculating part 1")
    for _ in range(times):
        temp_data = []
        for i in range(1, leng + 1):
            pat = get_pattern(i, leng)
            temp_data.append(abs(sum(si * pv for si, pv in zip(signal, pat))) % 10)
        signal = temp_data
        t.update()
    t.close()
    return signal


def main():
    day = get_script_file_name()

    with open(input_fp(day), "r") as f:
        data = [int(i) for i in f.read().strip()]

    # part 1
    res_print(day, 1, "".join(str(i) for i in run_fft(data.copy(), 100)[:8]))

    # part 2
    offset = int("".join(str(i) for i in data[:7]))
    data_2 = data * 10000
    data_2 = data_2[offset:]  # pattern until offset will be all zeros, so can be ignored
    leng = len(data_2)

    t = tqdm(total=100)
    t.set_description("Calculating part 2")
    for _ in range(100):
        temp_data = []
        total_sum = sum(data_2)
        temp_data.append(total_sum % 10)
        for i in range(1, leng):
            total_sum -= data_2[i - 1]
            temp_data.append(total_sum % 10)
        data_2 = temp_data
        t.update()
    t.close()

    res_print(day, 2, "".join(str(i) for i in data_2[:8]))


if __name__ == '__main__':
    main()
