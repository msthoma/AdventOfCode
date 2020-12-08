import re

from utils import utils


def main():
    # import/process day get_data
    data = utils.get_data(2020, 6)
    answer_a, answer_b = 0, 0
    # split get_data at empty lines
    for entry in re.compile(r"^$", flags=re.MULTILINE).split(data):
        # part a
        answer_a += len(set(entry.replace("\n", "")))

        # part b
        entry = map(set, entry.strip().split("\n"))
        answer_b += len(set.intersection(*entry))

    print("Answer part a:", answer_a)
    print("Answer part b:", answer_b)


if __name__ == '__main__':
    main()
