from utils.utils import day_name, input_fp, print_res


def get_pattern(i, leng):
    base_pat = [0, 1, 0, -1]
    pat, j = [], 0
    while len(pat) <= leng:
        pat.extend([base_pat[j % len(base_pat)]] * i)
        j += 1
    return pat[1:leng + 1]


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        data = [int(i) for i in f.read().strip()]

    # part 1
    data_1 = data.copy()
    leng = len(data_1)
    for _ in range(100):
        temp_data = []
        for i, v in enumerate(data_1):
            pat = get_pattern(i + 1, leng)
            assert len(pat) >= leng
            temp_data.append(abs(sum(si * pv for si, pv in zip(data_1, pat))) % 10)
        data_1 = temp_data

    print_res(day, 1, "".join(str(i) for i in data_1[:8]))

    # part 2


if __name__ == '__main__':
    main()
