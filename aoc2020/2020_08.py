from utils import utils


def run_code(code: list, part: str = "a"):
    accumulator, current, executed, code_len = 0, 0, set(), len(code)

    while current < code_len:
        if current in executed:
            if part == "a":
                return accumulator
            else:
                return None

        executed.add(current)
        instr, val = code[current]

        if instr == "acc":
            accumulator += val
            current += 1
        elif instr == "jmp":
            current += val
        elif instr == "nop":
            current += 1

    return accumulator


def main():
    data = [line.split(" ") for line in utils.get_data_for_day().splitlines()]
    code = [[i, int(j)] for i, j in data]

    # part a
    print("Answer part a:", run_code(code, part="a"))

    # part b
    for i, (instr, val) in enumerate(code):
        if instr == "acc":
            continue
        # swap jmp <-> nop, generate new code
        new_instr = "jmp" if instr == "nop" else "nop"
        new_code = code[:i] + [[new_instr, val]] + code[i + 1:]
        # run new code, print answer if it's not None
        if (res := run_code(new_code, part="b")) is not None:
            print("Answer part b:", res)


if __name__ == '__main__':
    main()
