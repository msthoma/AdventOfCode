from collections import deque

from utils.utils import get_data, res_print2


def main():
    deck_1, deck_2 = map(
        lambda x: list(map(int, x.split(":\n")[1].splitlines())),
        get_data().split("\n\n"))
    deck_1a, deck_2a = map(deque, [deck_1, deck_2])
    deck_1a = deque(deck_1a)

    while len(deck_1a) != 0 and len(deck_2a) != 0:
        card_1, card_2 = deck_1a.popleft(), deck_2a.popleft()
        if card_1 > card_2:
            deck_1a.extend([card_1, card_2])
        else:
            deck_2a.extend([card_2, card_1])

    winner = deck_1a if len(deck_1a) > len(deck_2a) else deck_2a

    winner_score = 0
    for i, card in enumerate(reversed(winner)):
        winner_score += card * (i + 1)

    res_print2(winner_score, 1)
    res_print2(2, 2)


if __name__ == '__main__':
    main()
