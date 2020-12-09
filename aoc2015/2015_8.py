import re

from utils.utils import get_data, res_print2


def main():
    data = get_data()
    data_code = data.replace("\n", "")

    # part a
    data_mem = "".join(l[1:-1] for l in data.splitlines())  # remove ""
    data_mem = data_mem.replace('\\"', ";").replace("\\\\", ";")
    data_mem = re.sub(r"\\x\w\w", ";", data_mem)

    # simpler solution for part a
    answer_1 = sum(len(l) - len(eval(l)) for l in data.splitlines())

    # part b
    data_str = data.splitlines()
    data_str = [d.replace('\\\\', "aaaa") for d in data_str]
    data_str = [d.replace('\\"', '\\\\\\"') for d in data_str]
    data_str = [re.sub(r"\\x[0-9A-Fa-f]{2}", r'\\\\xxx', d) for d in data_str]
    data_str = [re.sub(r'^\"', '"\\"', d) for d in data_str]
    data_str = [re.sub(r'\"$', '\\""', d) for d in data_str]

    # simpler solution for part b
    answer2 = sum(d.count("\\") + d.count('"') + 2 for d in data.splitlines())

    res_print2(len(data_code) - len(data_mem), 1)
    res_print2(answer_1, 1)
    res_print2(len("".join(data_str)) - len(data_code), 2)
    res_print2(answer2, 2)


if __name__ == '__main__':
    main()
