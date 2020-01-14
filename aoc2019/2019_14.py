import re
from collections import defaultdict

from utils.utils import day_name, input_fp, print_res


def get_reqs(reactions, fuel_amount=1, target="ORE"):
    needed = {"FUEL": fuel_amount}
    have = defaultdict(int)

    while True:
        try:
            needed_ing = next(ing for ing in needed if ing != target)
        except StopIteration:
            break

        q_needed = reactions[needed_ing]["amount"]

        created = needed[needed_ing] // q_needed
        still_needed = needed[needed_ing] % q_needed

        if still_needed == 0:  # fulfilled need for ingredient
            del needed[needed_ing]
        else:
            del needed[needed_ing]
            have[needed_ing] = q_needed - still_needed
            created += 1

        for ing, q in reactions[needed_ing].items():
            if ing == "amount":
                continue
            needed[ing] = needed.get(ing, 0) - have[ing] + q * created
            del have[ing]

    return needed[target]


def main():
    day = day_name()

    pattern = re.compile(r"(\d+) ([A-Z]+)")

    with open(input_fp(day), "r") as f:
        data = [line.strip("\n") for line in f.readlines()]

    data = [re.findall(pattern, line) for line in data]

    # part 1
    reactions = {}
    for reaction in data:
        reaction = [(int(q), m) for q, m in reaction]
        reactions[reaction[-1][1]] = {k: v for v, k in reaction[:-1]}
        reactions[reaction[-1][1]]["amount"] = reaction[-1][0]

    print_res(day, 1, get_reqs(reactions, fuel_amount=1))

    # part 2 - binary search to maximum FUEL with a trillion ORE
    goal = 1000000000000
    minimum, maximum = 1, 2
    while get_reqs(reactions, fuel_amount=maximum) < goal:
        minimum = maximum
        maximum = maximum * 2
    while maximum - minimum >= 2:
        mid = minimum + (maximum - minimum) // 2
        if get_reqs(reactions, fuel_amount=mid) > goal:
            maximum = mid
        else:
            minimum = mid

    print_res(day, 2, minimum)


if __name__ == '__main__':
    main()
