from utils.utils import get_script_file_name, input_fp, res_print


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()
    res_print(day, 1, input_data.count("(") - input_data.count(")"))

    pos = 0
    for i, instr in enumerate(input_data):
        if instr == "(":
            pos += 1
        elif instr == ")":
            pos -= 1

        if pos < 0:
            res_print(day, 2, i + 1)
            break


if __name__ == '__main__':
    main()
