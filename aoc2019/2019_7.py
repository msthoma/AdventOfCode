from itertools import permutations

from aoc2019.intcode import computer
from utils.utils import day_name, input_fp, print_res


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        intcode = [int(i) for i in f.read().split(sep=",")]

    # part 1
    part1_res = {}
    for comb in permutations(range(5)):
        input_signal = 0
        for phase in comb:
            res = computer(intcode.copy(), [phase, input_signal])
            input_signal = res["output"][-1]
        part1_res[comb] = input_signal

    print_res(day, 1, max(part1_res.values()))

    # part 2
    amps = "ABCDE"
    part2_res = []
    for phases in permutations(range(5, 10)):
        program_states = {k: 0 for k in amps}
        programs = {k: intcode.copy() for k in amps}
        input_signal = 0
        halt = False
        phases = iter(phases)
        while not halt:
            for amp in amps:
                if program_states[amp] == 0:
                    res = computer(programs[amp], [next(phases), input_signal], feedback=True)
                else:
                    res = computer(programs[amp], [input_signal], ip=program_states[amp], feedback=True)
                if res["halt"]:
                    halt = res["halt"]
                    break
                input_signal = res["output"][-1]
                program_states[amp] = res["ip"]
        part2_res.append(input_signal)

    print_res(day, 2, max(part2_res))


if __name__ == '__main__':
    main()
