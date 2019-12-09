from utils import utils


def computer2(intcode, ip=0):
    opcode = intcode[ip]
    # print("opcode", opcode)
    if opcode == 99:
        # terminate
        return intcode
    else:
        opcode_str = str(opcode)
        opcode = int(opcode_str[-1])
        assert opcode in [1, 2, 3, 4]

        if opcode == 3:
            intcode[intcode[ip + 1]] = int(input("Enter integer input: "))
            ip += 2
        elif opcode == 4:
            print("output:", intcode[intcode[ip + 1]])
            ip += 2
        else:
            modes = [0] * 3
            for i, mode in enumerate(opcode_str[:-2][::-1]):
                mode = int(mode)
                assert mode in [0, 1]
                modes[i] = mode

            # print(modes)

            p1 = intcode[intcode[ip + 1]] if modes[0] == 0 else intcode[ip + 1]
            p2 = intcode[intcode[ip + 2]] if modes[1] == 0 else intcode[ip + 2]

            if opcode == 1:
                intcode[intcode[ip + 3]] = p1 + p2
            elif opcode == 2:
                intcode[intcode[ip + 3]] = p1 * p2
            ip += 4

    return computer2(intcode, ip)


def main():
    day = utils.get_day_name()
    with open(f"{day}.txt", "r") as f:
        input_data = f.read().split(sep=",")

    input_data = [int(i) for i in input_data]

    res = computer2(input_data)
    print(res)


if __name__ == '__main__':
    main()
