def computer(intcode, pos=0):
    start_pos = pos * 4
    opcode = intcode[start_pos]

    if opcode == 99:
        return intcode
    elif opcode == 1:
        intcode[intcode[start_pos + 3]] = intcode[intcode[start_pos + 1]] + intcode[intcode[start_pos + 2]]
    elif opcode == 2:
        intcode[intcode[start_pos + 3]] = intcode[intcode[start_pos + 1]] * intcode[intcode[start_pos + 2]]
    else:
        return intcode

    pos += 1

    return computer(intcode, pos)


def run_program(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    return computer(intcode)[0]


def combinations(start, stop):
    # comb = []
    # for i in range(start, stop + 1):
    #     for j in range(start, stop + 1):
    #         comb.append([i, j])
    return ([j, i] for j in range(start, stop + 1) for i in range(start, stop + 1))


def main():
    with open("day2_input.txt", "r") as f:
        input_data = f.read().split(sep=",")

    input_data = [int(i) for i in input_data]

    print("day 2, part 1:", run_program(input_data.copy(), 12, 2))

    for cmb in combinations(0, 99):
        res = run_program(input_data.copy(), cmb[0], cmb[1])
        if res == 19690720:
            print("day 2, part 2:", cmb, 100 * cmb[0] + cmb[1])
            break

    # print(combinations(0, 99))


if __name__ == '__main__':
    main()
