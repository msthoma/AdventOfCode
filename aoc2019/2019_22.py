from utils.utils import day_name, input_fp, print_res


def deal_increment(deck, increment):
    n_deck = [0] * len(deck)
    position = 0
    for card in deck:
        n_deck[position] = card
        position = (position + increment) % (len(deck))
    return n_deck


def cut_deck(deck, n):
    n_deck = deck[n:].copy()
    n_deck.extend(deck[:n])
    return n_deck


def deal_new_stack(deck):
    return list(reversed(deck))


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        instructions = (line.strip() for line in f.readlines())

    # part 1
    deck = [i for i in range(10007)]
    for instruction in instructions:
        if "increment" in instruction:
            increment = int(instruction.lstrip("deal with increment "))
            deck = deal_increment(deck, increment)
        elif "cut" in instruction:
            n = int(instruction.lstrip("cut "))
            deck = cut_deck(deck, n)
        elif "new" in instruction:
            deck = deal_new_stack(deck)

    print_res(day, 1, deck.index(2019))

    # part 2


if __name__ == '__main__':
    main()
