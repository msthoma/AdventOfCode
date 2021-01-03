import re

from utils.utils import get_data, res_print2


def do_strange_math_a(formula):
    if type(formula) is re.Match:
        formula = formula.group(0)

    formula = formula.strip("()")

    first = re.compile(r"^\d+? [*|+] \d+")

    while any(p in formula for p in ["*", "+"]):
        start = first.match(formula)
        if not start:
            break
        start_eval, end = eval(start.group(0)), ""
        if len(formula) > 3:
            end = formula[start.end():]
        formula = str(start_eval) + end

    return formula


def main():
    data = get_data().splitlines()

    # pattern for substrings in parentheses but do not contain inner parentheses
    in_parentheses = re.compile(r"\([^(]+?\)")

    while True:
        new_data = []
        for line in data:
            if type(line) is not int:
                if "(" in str(line):
                    line = re.sub(in_parentheses, repl=do_strange_math_a,
                                  string=line)
                else:
                    line = int(do_strange_math_a(line))
            new_data.append(line)
        data = new_data

        if all(map(lambda x: type(x) is int, data)):
            answer_a = sum(data)
            break

    res_print2(answer_a, 1)
    res_print2(2, 2)


if __name__ == '__main__':
    main()
