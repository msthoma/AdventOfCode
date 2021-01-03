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

    nearby_tickets = [list(map(int, t.split(","))) for t in
                      data[data.index("nearby tickets:") + 1:]]
    valid_tickets = []
    error_rate = 0

    # calculate error rate for part a, remove invalid tickets for part b
    for ticket in nearby_tickets:
        valid = True
        for num in ticket:
            if num not in valid_nums:
                error_rate += num
                valid = False
        if valid:
            valid_tickets.append(ticket)

    valid_tickets = np.array(valid_tickets)

    # determine candidate fields for each category (column in valid_tickets.T)
    categories = {}
    for i, cat_vals in enumerate(valid_tickets.T):
        cat_vals = set(cat_vals)
        candidates = list(valid_nums_by_field.keys())
        for field, valid_n in valid_nums_by_field.items():
            if not cat_vals.issubset(valid_n):
                candidates.remove(field)
        categories[i] = candidates

    # determine actual field for each category by elimination
    category_determined = {}
    remaining = categories.copy()
    while len(category_determined) != len(categories):
        for cat, fields in remaining.items():
            if len(fields) == 1:
                category_determined[fields[0]] = cat
                for c, f in remaining.items():
                    try:
                        remaining[c] = [v for v in f if v != fields[0]]
                    except Exception:
                        pass
                break

    # get my ticket and calculate part b answer
    my_ticket = [int(i) for i in
                 data[data.index("your ticket:") + 1].split(",")]
    answer_part_b = 1
    for k in category_determined.keys():
        if "departure" in k:
            answer_part_b *= my_ticket[category_determined[k]]

    res_print2(error_rate, 1)
    res_print2(answer_part_b, 2)


if __name__ == '__main__':
    main()
