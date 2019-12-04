import os
import sys

day_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]


def main():
    with open(f"{day_name}.txt", "r") as f:
        input_data = f.read()
    print(f"{day_name}_1 answer:", input_data.count("(") - input_data.count(")"))

    pos = 0
    for i, instr in enumerate(input_data):
        if instr == "(":
            pos += 1
        elif instr == ")":
            pos -= 1

        if pos < 0:
            print(f"{day_name}_2 answer:", i + 1)
            break


if __name__ == '__main__':
    main()
