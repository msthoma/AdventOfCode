from utils import utils


def find_row_col(code: str, n_rows: int = 128, n_cols: int = 8):
    rows, cols = list(range(n_rows)), list(range(n_cols))
    answer = []

    for ar, cd in zip([rows, cols], [code[:7], code[7:]]):
        for c in cd:
            middle = len(ar) // 2
            if c in "FL":
                ar = ar[:middle]
            else:
                ar = ar[middle:]
        assert len(ar) == 1
        answer.append(ar[0])

    answer.append(answer[0] * 8 + answer[1])

    return answer


def main():
    # import/process day get_data_for_day
    data = utils.get_data_for_day(2020, 5).splitlines()
    assert all(len(s) == 10 for s in data)

    seat_ids = sorted(find_row_col(code)[-1] for code in data)
    print("Answer part a:", max(seat_ids))

    for i, seat_id in enumerate(seat_ids):
        if i == 0:
            continue
        if seat_id - seat_ids[i - 1] > 1:
            print("Answer part b:", seat_id - 1)
            break


if __name__ == '__main__':
    main()
