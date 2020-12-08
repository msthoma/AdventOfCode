from utils.utils import get_data, res_print2


def main():
    input_data = get_data()

    res_print2(input_data.count("(") - input_data.count(")"), 1)

    pos = 0
    for i, instr in enumerate(input_data):
        if instr == "(":
            pos += 1
        elif instr == ")":
            pos -= 1

        if pos < 0:
            res_print2(i + 1, 2)
            break


if __name__ == '__main__':
    main()
