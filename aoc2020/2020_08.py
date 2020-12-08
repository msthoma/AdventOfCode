from utils import utils


def main():
    data = [line.split(" ") for line in utils.data(2020, 8).splitlines()]
    data = [[i, int(j)] for i, j in data]

    accumulator, current, executed = 0, 0, set()

    while True:
        if current in executed:
            break

        executed.add(current)
        instr, val = data[current]

        if instr == "acc":
            accumulator += val
            current += 1
        elif instr == "jmp":
            current += val
        elif instr == "nop":
            current += 1

    print("Answer part a:", accumulator)
    print("Answer part b:", 0)


if __name__ == '__main__':
    main()
