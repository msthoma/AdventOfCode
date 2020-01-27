from utils.utils import day_name, input_fp


def main():
    day = day_name()

    with open(input_fp(day), "r") as f:
        instructions = (line.strip() for line in f.readlines())

    print(list(instructions))

    # part 1

    # part 2


if __name__ == '__main__':
    main()
