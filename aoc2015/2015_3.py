from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()
    print(len(input_data))

    houses = [[0, 0]]
    for i, move in enumerate(input_data):
        previous_pos = houses[i]


if __name__ == '__main__':
    main()
