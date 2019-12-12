from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()
    print_res(day, 1, input_data.count("(") - input_data.count(")"))

    pos = 0
    for i, instr in enumerate(input_data):
        if instr == "(":
            pos += 1
        elif instr == ")":
            pos -= 1

        if pos < 0:
            print_res(day, 2, i + 1)
            break


if __name__ == '__main__':
    main()
