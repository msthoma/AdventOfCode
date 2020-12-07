from utils import utils


def main():
    # import/process day data
    data = utils.data(2020, 2)
    data = [line.replace(":", "").split(" ") for line in data.splitlines()]
    data = [[a.split("-"), b, c] for a, b, c in data]
    for k, _, _ in data:
        assert len(k) == 2

    # part a
    answer_a = 0
    for (low, high), letter, pwd in data:
        # print(low, high, letter, pwd, pwd.count(letter),
        #       pwd.count(letter) in range(int(low), int(high) + 1))
        if pwd.count(letter) in range(int(low), int(high) + 1):
            answer_a += 1
    print("Answer part a:", answer_a)

    # part b
    answer_b = 0
    for (first, second), letter, pwd in data:
        # -1 to account for non-zero index
        first, second = int(first) - 1, int(second) - 1
        first, second = pwd[first], pwd[second]

        if (first == letter or second == letter) and first != second:
            answer_b += 1

    print("Answer part b:", answer_b)


if __name__ == '__main__':
    main()
