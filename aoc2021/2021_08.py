import time

from utils.utils import res_print2, get_data

if __name__ == '__main__':
    data = [[p.split(" ") for p in line.split(" | ")] for line in get_data().splitlines()]

    start = time.time()
    unique_lengths = [2, 3, 4, 7]
    p1 = sum(sum(len(o) in unique_lengths for o in outputs) for _, outputs in data)
    res_print2(p1, 1, start)

    # Steps for part 2:
    # start
    #    1,       4,       7, 8
    # only remaining that is superset of 4 -> 9
    #    1,       4,       7, 8, 9
    # six letter numbers can be only 0 and 6 -> from these, the one that is superset of 1 is 0, and the other 6
    # 0, 1,       4,    6, 7, 8, 9
    # from five letter numbers, the one that is superset of 1 is 3
    # 0, 1,    3, 4,    6, 7, 8, 9
    # 2 and 5 remaining, the one that is subset of 9 is 5, the other 2
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    start = time.time()
    output_sum = 0
    for io in data:
        inputs, outputs = io
        unique_inputs = [i for i in inputs if len(i) in unique_lengths]
        remaining = [i for i in inputs if len(i) not in unique_lengths]

        # find 1, 7, 4 and 8
        n = {}
        for i in unique_inputs:
            if len(i) == 2:
                n[1] = i
            elif len(i) == 3:
                n[7] = i
            elif len(i) == 4:
                n[4] = i
            elif len(i) == 7:
                n[8] = i
            else:
                raise ValueError

        # find 9
        nine = [i for i in remaining if set(i).issuperset(n[4])]
        assert len(nine) == 1
        n[9] = nine[0]
        remaining.remove(n[9])

        for i in remaining:
            if len(i) == 5:
                # disambiguate 2, 3 and 5
                if set(i).issuperset(n[1]):
                    n[3] = i
                else:
                    # disambiguate 2 and 5
                    if set(i).issubset(n[9]):
                        n[5] = i
                    else:
                        n[2] = i
            elif len(i) == 6:
                # disambiguate 0 and 6
                if set(i).issuperset(n[1]):
                    n[0] = i
                else:
                    n[6] = i
            else:
                raise ValueError

        assert len(n) == 10

        n_letter_keys = {tuple(sorted(set(v))): k for k, v in n.items()}

        outputs_translated = [n_letter_keys[tuple(sorted(set(o)))] for o in outputs]

        output_sum += int("".join(map(str, outputs_translated)))

    res_print2(output_sum, 2, start)
