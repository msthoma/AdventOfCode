from utils.utils import day_name, input_fp, print_res


def shuffle(deck, instructions):
    for instruction in instructions:
        if "increment" in instruction:
            increment = int(instruction.lstrip("deal with increment "))
            deck = deal_increment(deck, increment)
        elif "cut" in instruction:
            n = int(instruction.lstrip("cut "))
            deck = cut_deck(deck, n)
        elif "new" in instruction:
            deck = deal_new_stack(deck)
    return deck


def deal_increment(deck, increment):
    n_deck = [0] * len(deck)
    position = 0
    for card in deck:
        n_deck[position] = card
        position = (position + increment) % (len(deck))
    return n_deck


def cut_deck(deck, n):
    return deck[n:] + deck[:n]


def deal_new_stack(deck):
    return list(reversed(deck))


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        instructions = (line.strip() for line in f.readlines())

    # part 1
    deck_1 = shuffle([i for i in range(10007)], instructions)
    print_res(day, 1, deck_1.index(2019))

    # part 2


if __name__ == '__main__':
    main()
