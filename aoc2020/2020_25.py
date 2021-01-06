from utils.utils import res_print2, get_data


def find_loop_size(initial_sub_n: int, public_key: int):
    t = transform(initial_sub_n)
    while True:
        loop_size, value = next(t)
        if value == public_key:
            return loop_size


def transform_n_loop_times(sub_n: int, loop_size: int):
    t = transform(sub_n)
    for _ in range(loop_size - 1):
        _, _ = next(t)
    loop_size, value = next(t)
    return loop_size, value


def transform(sub_n):
    value, loop_size = 1, 1
    while True:
        value = value * sub_n
        value = value % 20201227
        yield loop_size, value
        loop_size += 1


def main():
    card_public, door_public = map(int, get_data().splitlines())

    card_loop_size = find_loop_size(7, card_public)
    door_loop_size = find_loop_size(7, door_public)

    _, encryption_key_card = transform_n_loop_times(door_public, card_loop_size)
    _, encryption_key_door = transform_n_loop_times(card_public, door_loop_size)

    assert encryption_key_card == encryption_key_door

    res_print2(encryption_key_card, 1)
    res_print2(2, 2)


if __name__ == '__main__':
    main()
