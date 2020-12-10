from utils.utils import get_data, res_print2


def look_and_say(seq: str):
    cur, new_number = [], []
    for i, n in enumerate(seq):
        cur.append(n)
        if i < len(seq) - 1 and n == seq[i + 1]:
            continue
        else:
            new_number.append(str(len(cur)))
            new_number.append(str(cur[0]))
            cur.clear()
    return "".join(new_number)


def main():
    data = get_data()

    seq_a = data
    for _ in range(40):
        seq_a = look_and_say(seq_a)
    res_print2(len(seq_a), 1)

    seq_b = data
    for _ in range(50):
        seq_b = look_and_say(seq_b)
    res_print2(len(seq_b), 2)


if __name__ == '__main__':
    main()
