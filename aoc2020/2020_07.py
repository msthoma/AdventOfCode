import re
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

from utils import utils


def count_bags_in(bag: str, g: nx.DiGraph):
    bag_count = 0
    for bag, val in g[bag].items():
        bag_count += val["n"]
        bag_count += val["n"] * count_bags_in(bag, g)
    return bag_count


def main():
    data = utils.get_data_for_day(2020, 7).splitlines()

    pattern = re.compile(r"(^|\d|no) ?(.+?) bag")

    rules = defaultdict(dict)

    # put rules dictionary
    for rule in data:
        rule = pattern.findall(rule)
        empty, colour = rule[0]
        assert empty == ""  # 1st component's 1st element should be ""
        for n, inner_colour in rule[1:]:
            if n == "no":  # handle 'no other' rule
                pass
            else:
                rules[colour][inner_colour] = int(n)

    # convert rules into graph
    g = nx.DiGraph()
    for parent, children in rules.items():
        for child, n in children.items():
            g.add_edge(parent, child, n=n)

    plt.figure(figsize=(20, 20))
    nx.draw(g, with_labels=True)
    plt.show()

    print("Answer part a:", len(nx.ancestors(g, source="shiny gold")))
    print("Answer part b:", count_bags_in(bag="shiny gold", g=g))


if __name__ == '__main__':
    main()
