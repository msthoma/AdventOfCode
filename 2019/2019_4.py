import os
import re
import sys

day_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]


def main():
    puzzle_input = range(372304, 847060 + 1)
    candidates = 0
    candidates_2 = 0
    pattern = re.compile(r"(\d)\1+")
    pattern_2 = re.compile(r"(\d)\1{2,}")
    for pwd in puzzle_input:
        pwd = str(pwd)
        if re.search(pattern, pwd):
            if not any([int(l) - int(pwd[i]) < 0 for i, l in enumerate(pwd[1:])]):
                candidates += 1
                if not re.search(pattern_2, pwd):
                    candidates_2 += 1
                else:
                    pwd_sub = re.sub(pattern_2, " ", pwd)
                    if re.search(pattern, pwd_sub):
                        candidates_2 += 1

    print(f"{day_name}_1 answer:", candidates)
    print(f"{day_name}_2 answer:", candidates_2)


if __name__ == '__main__':
    main()
