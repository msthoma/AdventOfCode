from utils import utils


def recursive_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


def main():
    day_name = utils.get_day_name()
    with open(f"{day_name}.txt", "r") as f:
        input_data = f.read().splitlines()

    utils.print_res(day_name, 1, sum((int(i) // 3) - 2 for i in input_data))
    utils.print_res(day_name, 1, sum(recursive_fuel(int(i)) for i in input_data))


if __name__ == '__main__':
    main()
