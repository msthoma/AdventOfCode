from utils import utils


def run_code(code: list):
    accumulator, current, executed = 0, 0, set()

    while True:
        if current in executed:
            break

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
    data = [line.split(" ") for line in utils.data(2020, 8).splitlines()]
    code = [[i, int(j)] for i, j in data]

    print("Answer part a:", run_code(code))
    print("Answer part b:", 0)


if __name__ == '__main__':
    main()
