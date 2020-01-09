import re

from utils.utils import day_name, input_fp


def main():
    day = day_name()

    pattern = re.compile(r"(\d+) ([A-Z]+)")

    with open(input_fp(day), "r") as f:
        data = [line.strip("\n") for line in f.readlines()]

    data = [re.findall(pattern, line) for line in data]

    print(data)

    # part 1
    reactions = []
    for reaction in data:
        reaction = [(int(q), m) for q, m in reaction]
        reactions.append(reaction)

    print(reactions)


if __name__ == '__main__':
    main()
