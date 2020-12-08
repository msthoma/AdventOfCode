from utils.utils import get_script_file_name, input_fp, res_print


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()
    print(len(input_data))

    houses = [[0, 0]]
    for i, move in enumerate(input_data):
        previous_pos = houses[i]


if __name__ == '__main__':
    main()
