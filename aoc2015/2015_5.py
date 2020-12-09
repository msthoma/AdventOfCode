import re

from utils.utils import get_data, res_print2


def main():
    data = get_data().splitlines()

    # part a rules
    disallowed = re.compile(r"(ab|cd|pq|xy)")
    contains_repeat = re.compile(r"([a-z])\1+")

    # part b rules
    b_first_rule = re.compile(r"(\w{2})(?:.*?)\1+")
    b_second_rule = re.compile(r"(\w).\1")

    nice_a, nice_b = 0, 0
    for strg in data:
        if not disallowed.search(strg):
            if contains_repeat.search(strg):
                if sum(map(strg.count, "aeiou")) >= 3:
                    nice_a += 1
        if b_first_rule.search(strg) and b_second_rule.search(strg):
            nice_b += 1

    res_print2(nice_a, 1)
    res_print2(nice_b, 2)


if __name__ == '__main__':
    main()
