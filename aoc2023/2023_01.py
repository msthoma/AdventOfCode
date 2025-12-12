from utils.utils import res_print2, get_data


def calibration(line: str) -> int:
    nums = [c for c in line if c.isdigit()]
    return int(f"{nums[0]}{nums[-1]}")


def main():
    data = get_data()

    part_a = [calibration(line) for line in data.splitlines()]
    res_print2(sum(part_a), part=1)

    str_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for k, v in str_numbers.items():
        data = data.replace(k, f"{k}{v}{k}")

    part_b = [calibration(line) for line in data.splitlines()]
    res_print2(sum(part_b), part=2)


if __name__ == "__main__":
    main()
