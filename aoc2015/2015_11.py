import re
from string import ascii_lowercase as letters

from more_itertools import windowed as win

from utils.utils import get_data, res_print2


class IsValid(object):
    def __init__(self):
        self.pairs = re.compile(r"(\w)(\1).*?(\w)(\3)")

    def check(self, pwd: list):
        if any(lt in pwd for lt in "iol"):  # forbidden chars
            return False
        else:
            # contains at least 2 different, non-overlapping pairs of letters
            # includes at least 1 increasing straight of at least three letters
            pwd = "".join(pwd)
            return bool(self.pairs.search(pwd)) and any(
                "".join(i) in pwd for i in win(letters, 3))


def next_potentially_valid(pwd: list):
    new_pwd = []
    for i, lt in enumerate(pwd):
        if lt not in "iol":
            new_pwd.append(lt)
        else:
            new_pwd.append({"i": "j", "l": "m", "o": "p"}[lt])
            new_pwd.extend(["a"] * (len(pwd) - i - 1))
            break
    assert len(pwd) == len(new_pwd)
    return new_pwd


def increment(pwd: list):
    if any(lt in pwd for lt in "iol"):
        pwd = next_potentially_valid(pwd)

    valid = False
    is_valid = IsValid()

    while not valid:
        # index of letter currently incrementing, start at end
        incr_i = len(pwd) - 1
        while True:
            next_letter_index = (letters.index(pwd[incr_i]) + 1) % len(letters)
            pwd[incr_i] = letters[next_letter_index]
            if next_letter_index == 0:
                # if next letter was a, i.e. there was a wrap around, increment
                # letter to left as well
                incr_i -= 1
            else:
                break
        if any(lt in pwd for lt in "iol"):
            pwd = next_potentially_valid(pwd)

        valid = is_valid.check(pwd)

    return pwd


def main():
    data = list(get_data())

    answer_1 = increment(data)

    res_print2("".join(answer_1), 1)
    res_print2("".join(increment(answer_1)), 2)


if __name__ == '__main__':
    main()
