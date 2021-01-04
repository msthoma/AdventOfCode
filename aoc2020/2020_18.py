import re

from utils.utils import get_data, res_print2


def do_math_part_a(formula):
    if type(formula) is re.Match:
        formula = formula.group(0)

    formula = formula.strip("()")

    first = re.compile(r"^\d+? [*|+] \d+")

    while any(o in formula for o in ["*", "+"]):
        start = first.match(formula)
        if not start:
            break
        start_eval, end = eval(start.group(0)), ""
        if len(formula) > 3:
            end = formula[start.end():]
        formula = str(start_eval) + end

    return formula


def do_addition(formula: re.Match):
    if type(formula) is re.Match:
        formula = formula.group(0)
    assert "+" in formula
    return str(eval(formula))


def do_math_part_b(formula):
    if type(formula) is re.Match:
        formula = formula.group(0)

    formula = formula.strip("()")

    addition = re.compile(r"\d+? \+ \d+")

    while "+" in formula:
        formula = re.sub(addition, repl=do_addition, string=formula,
                         count=1)
    formula = str(eval(formula))
    return formula


def solve_with_rules(rules, data: list):
    # pattern for substrings in parentheses but do not contain inner parentheses
    in_parentheses = re.compile(r"\([^(]+?\)")

    while True:
        new_data = []
        for line in data:
            if type(line) is not int:
                if "(" in str(line):
                    line = re.sub(in_parentheses, repl=rules, string=line)
                else:
                    line = int(rules(line))
            new_data.append(line)
        data = new_data

        if all(map(lambda x: type(x) is int, data)):
            return sum(data)


def main():
    data = get_data().splitlines()

    res_print2(solve_with_rules(do_math_part_a, data.copy()), 1)
    res_print2(solve_with_rules(do_math_part_b, data.copy()), 2)


if __name__ == '__main__':
    main()
