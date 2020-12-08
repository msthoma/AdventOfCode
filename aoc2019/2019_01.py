from utils.utils import get_script_file_name, input_fp, res_print


def recursive_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()

    res_print(day, 1, sum((int(i) // 3) - 2 for i in input_data))
    res_print(day, 1, sum(recursive_fuel(int(i)) for i in input_data))


if __name__ == '__main__':
    main()
