from collections import defaultdict

from utils.utils import get_data, res_print2


def main():
    data = get_data().splitlines()
    part_a, part_b = {}, {}

    for i, (winning, numbers_have) in enumerate(
        [c.split(":")[1].strip().split(" | ") for c in data], start=1
    ):
        winning = [int(n) for n in winning.split(" ") if n]
        numbers_have = [int(n) for n in numbers_have.split(" ") if n]
        intersection = set(numbers_have).intersection(set(winning))
        part_a[i] = 0 if not intersection else 2 ** (len(intersection) - 1)
        part_b[i] = len(intersection)

    res_print2(sum(part_a.values()), part=1)

    original_cards = list(part_a.keys())

    part_b_queue = defaultdict(int)
    part_b_final_cards = defaultdict(int)

    for card in original_cards:
        part_b_queue[card] += 1

    for card, n_cards in part_b_queue.items():
        part_b_final_cards[card] += n_cards
        part_b_queue[card] = 0
        card_score = part_b[card]
        for new_card in original_cards[card : card + card_score]:
            part_b_queue[new_card] += n_cards

    res_print2(sum(part_b_final_cards.values()), part=2)


if __name__ == "__main__":
    main()
