import re

from utils.utils import get_data, res_print2


def solve_instr_dict(instr_dict: dict):
    solved = set()
    i = 0
    while len(solved) != len(instr_dict):
        for k, v in instr_dict.items():
            if type(v) is int:
                # already solved
                continue
            try:
                v = solve_instr(v, instr_dict, solved)
                instr_dict[k] = v
                solved.add(k)
            except ValueError:
                # not solved yet
                pass
        i += 1
        if i > 2000:
            raise AssertionError("Seems to be looping infinitely!")
    return instr_dict


def solve_instr(instr, all_instr: dict, solved: set):
    if instr.isdigit():
        # cases where instruction is just a number
        return int(instr)

    get_vars = re.compile(r"([a-z]+|\d+)")
    get_gate = re.compile(r"([A-Z]+)")

    variables = get_vars.findall(instr)
    assert len(variables) <= 2

    if all(v in solved or v.isdigit() for v in variables):
        variables = [int(v) if v.isdigit() else all_instr[v] for v in variables]
        gate = get_gate.findall(instr)

        if len(gate) == 0:
            # case where a var is simply equal to another var (e.g. a->lx)
            if len(variables) == 1:
                return variables[0]

        assert len(gate) == 1
        gate = gate[0]

        if "SHIFT" in gate:
            if "L" in gate:
                return variables[0] << variables[1]
            if "R" in gate:
                return variables[0] >> variables[1]
        elif "OR" in gate:
            return variables[0] | variables[1]
        elif "AND" in gate:
            return variables[0] & variables[1]
        elif "NOT" in gate:
            assert len(variables) == 1, (variables, gate)
            return bitwise_not_uint16(variables[0])
    raise ValueError


def bitwise_not_uint16(i: int):
    return 2 ** 16 - 1 - i


def main():
    pat = re.compile(r"(.+) -> ([a-z]+)")

    data = get_data().splitlines()
    data = [list(pat.match(r).groups()) for r in data]

    instr_dict_a = {k: v for v, k in data}
    instr_dict_b = instr_dict_a.copy()

    # part a
    instr_dict_a = solve_instr_dict(instr_dict_a)
    res_print2(instr_dict_a["a"], 1)

    # part b
    instr_dict_b["b"] = str(instr_dict_a["a"])  # new value for "b" from part 1
    instr_dict_b = solve_instr_dict(instr_dict_b)
    res_print2(instr_dict_b["a"], 2)


if __name__ == '__main__':
    main()
