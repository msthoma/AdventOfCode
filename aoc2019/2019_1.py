from utils.utils import day_name, input_fp, print_res


def recursive_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().splitlines()

    print_res(day, 1, sum((int(i) // 3) - 2 for i in input_data))
    print_res(day, 1, sum(recursive_fuel(int(i)) for i in input_data))


if __name__ == '__main__':
    main()
