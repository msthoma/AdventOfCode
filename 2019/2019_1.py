from utils import utils


def recursive_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


def day_1_1(data):
    print(sum((int(i) // 3) - 2 for i in data))


def day_1_2(data):
    print(sum(recursive_fuel(int(i)) for i in data))


def main():
    with open(f"{utils.get_day_name()}.txt", "r") as f:
        input_data = f.read().splitlines()

    day_1_1(input_data)
    day_1_2(input_data)
    # print(f"{day_name}_1 answer:", common.loc[1:, "manhattan"].min())


if __name__ == '__main__':
    main()
