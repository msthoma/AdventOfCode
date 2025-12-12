import math
from collections import defaultdict

from utils.utils import res_print2, get_data


def main():
    data = get_data().splitlines()

    part_a_limit = {"red": 12, "green": 13, "blue": 14}
    part_a, part_b = [], []

    for line in data:
        game_id, rest = line.lstrip("Game").split(":")
        game_id = int(game_id)

        games = defaultdict(list)
        for game in rest.strip().split(";"):
            for game_component in game.strip().split(","):
                n, colour = game_component.strip().split(" ")
                games[colour].append(int(n))

        if all([max(games[c]) <= max_c for c, max_c in part_a_limit.items()]):
            part_a.append(game_id)

        part_b.append(math.prod([max(ns) for ns in games.values()]))

    res_print2(sum(part_a), part=1)
    res_print2(sum(part_b), part=2)


if __name__ == "__main__":
    main()
