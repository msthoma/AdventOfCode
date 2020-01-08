from aoc2019 import intcode
from utils.utils import day_name, input_fp, print_res


# def computer(intcode, ip=0):
#     opcode = intcode[ip]
#
#     if opcode == 99:
#         # terminate
#         return intcode
#     else:
#         # extract opcode
#         opcode_str = str(opcode)
#         opcode = int(opcode_str[-1])
#         assert opcode in range(1, 9)
#
#         # get modes
#         modes = [0] * 3
#         if len(opcode_str) != 1:
#             for i, mode in enumerate(opcode_str[:-2][::-1]):
#                 mode = int(mode)
#                 assert mode in [0, 1]
#                 modes[i] = mode
#
#         if opcode == 3:
#             intcode[intcode[ip + 1]] = 5  # int(input("Enter integer input: "))
#             ip += 2
#         else:
#             # get parameters
#             p1 = intcode[intcode[ip + 1]] if modes[0] == 0 else intcode[ip + 1]
#
#             if opcode == 4:
#                 print("output:", p1)
#                 ip += 2
#
#             else:
#                 p2 = intcode[intcode[ip + 2]] if modes[1] == 0 else intcode[ip + 2]
#
#                 if opcode == 5:
#                     if p1 != 0:
#                         ip = p2
#                     else:
#                         ip += 3
#
#                 elif opcode == 6:
#                     if p1 == 0:
#                         ip = p2
#                     else:
#                         ip += 3
#
#                 elif opcode == 7:
#                     if p1 < p2:
#                         intcode[intcode[ip + 3]] = 1
#                     else:
#                         intcode[intcode[ip + 3]] = 0
#                     ip += 4
#
#                 elif opcode == 8:
#                     if p1 == p2:
#                         intcode[intcode[ip + 3]] = 1
#                     else:
#                         intcode[intcode[ip + 3]] = 0
#                     ip += 4
#
#                 else:
#                     if opcode == 1:
#                         intcode[intcode[ip + 3]] = p1 + p2
#                     elif opcode == 2:
#                         intcode[intcode[ip + 3]] = p1 * p2
#                     ip += 4
#
#     return computer(intcode, ip)


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read().split(sep=",")

    input_data = [int(i) for i in input_data]

    print_res(day, 1, intcode.computer(input_data.copy(), [1])["output"][-1])
    print_res(day, 2, intcode.computer(input_data.copy(), [5])["output"][-1])


if __name__ == '__main__':
    main()
