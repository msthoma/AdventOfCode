import re

from utils import utils


def main():
    # import/process day get_data
    data = utils.get_data(2020, 4)

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    req_fields = fields.copy()
    req_fields.remove("cid")
    req_fields = set(req_fields)

    answer_a, answer_b = 0, 0

    val_part_b = {"byr": lambda x: int(x) in range(1920, 2002 + 1),
                  "iyr": lambda x: int(x) in range(2010, 2020 + 1),
                  "eyr": lambda x: int(x) in range(2020, 2030 + 1),
                  "hgt": lambda x: val_hgt(x),
                  "hcl": lambda x: x.startswith("#") and len(
                      x[1:]) == 6 and is_hex(x[1:]),
                  "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn",
                                         "hzl", "oth"],
                  "pid": lambda x: x.isdigit() and len(x) == 9,
                  "cid": lambda _: True}

    # split get_data at empty lines
    for entry in re.compile(r"^$", flags=re.MULTILINE).split(data):
        entry = [f.split(":") for f in
                 entry.strip().replace("\n", " ").split(" ")]

        # check for non-compliant entry fields
        assert all(f[0] in fields for f in entry)

        if req_fields.issubset(set(f[0] for f in entry)):  # val for part a
            answer_a += 1
            if all(val_part_b[k](v) for k, v in entry):  # val for part b
                answer_b += 1

    print("Answer part a:", answer_a)
    print("Answer part b:", answer_b)


def val_hgt(hgt: str):
    if "cm" in hgt:
        hgt = hgt.replace("cm", "")
        if hgt.isdigit() and int(hgt) in range(150, 193 + 1):
            return True
    if "in" in hgt:
        hgt = hgt.replace("in", "")
        if hgt.isdigit() and int(hgt) in range(59, 76 + 1):
            return True
    return False


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
