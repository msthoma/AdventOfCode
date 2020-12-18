import re
from collections import defaultdict

import numpy as np

from utils.utils import get_data, res_print2


def main():
    data = get_data().splitlines()

    pat = re.compile(r"(.+): (\d+-\d+) or (\d+-\d+)")
    valid_nums, valid_nums_by_field = set(), defaultdict(set)
    for line in data:
        if r := pat.match(line):
            field_name, r1, r2 = r.groups()
            for m in [r1, r2]:
                x, y = list(map(int, m.split("-")))
                for num in range(x, y + 1):
                    valid_nums.add(num)
                    valid_nums_by_field[field_name].add(num)
    print(valid_nums_by_field)

    nearby_tickets = [list(map(int, t.split(","))) for t in
                      data[data.index("nearby tickets:") + 1:]]
    valid_tickets = []
    error_rate = 0

    for ticket in nearby_tickets:
        valid = True
        for num in ticket:
            if num not in valid_nums:
                error_rate += num
                valid = False
        if valid:
            valid_tickets.append(ticket)
    valid_tickets = np.array(valid_tickets)
    print(valid_tickets)
    print(valid_tickets.T)
    for i, cat in enumerate(valid_tickets.T):
        cat = set(cat)
        print("category", i, "\n", "##############################")
        candidates = list(valid_nums_by_field.keys())
        for field, valid_n in valid_nums_by_field.items():
            if not cat.issubset(valid_n):
                candidates.remove(field)
        print("candidates", candidates)

    res_print2(error_rate, 1)
    res_print2(2, 2)


if __name__ == '__main__':
    main()
