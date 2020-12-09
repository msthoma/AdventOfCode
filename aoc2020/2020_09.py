from itertools import combinations

from utils.utils import get_data, res_print2


def main():
    data = [int(i) for i in get_data().splitlines()]

    # part a
    answer_1 = 0
    for i in range(len(data)):
        target, valid = data[i + 25], False
        for comb in combinations(data[i:i + 25], 2):
            if sum(comb) == target:
                valid = True
                break
        if not valid:
            answer_1 = target
            res_print2(answer_1, 1)
            break

    # part b
    for i in range(1, len(data)):
        current = data[:i]
        answer_2 = None
        for j in reversed(range(len(current) + 1)):
            if sum(current[j:i]) == answer_1:
                current_sorted = sorted(current[j:i])
                answer_2 = current_sorted[0] + current_sorted[-1]
                res_print2(answer_2, 2)
                break
        if answer_2 is not None:
            break


if __name__ == '__main__':
    main()
