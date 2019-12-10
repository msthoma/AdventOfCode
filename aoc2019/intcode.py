def computer(intcode):
    valid_opcodes = list(range(1, 9))
    valid_opcodes.append(99)

    ip = 0

    def get_params(nparams):
        op_str = str(intcode[ip])

        modes = [0] * 3
        if len(op_str) != 1:
            for i, mode in enumerate(op_str[:-2][::-1]):
                mode = int(mode)
                assert mode in [0, 1]
                modes[i] = mode

        # get params
        params = []
        for i in range(0, nparams):
            param = intcode[ip + i]  # immediate case
            if modes[i] == 0 and i < nparams - 1:
                param = intcode[param]  # position case
            params.append(param)

        return params

    while True:
        opcode = intcode[ip] % 100
        print(opcode)
        assert opcode in valid_opcodes

        if opcode == 99:  # terminate
            break
        elif opcode == 1:  # add
            p1, p2, p3 = get_params(3)
            intcode[p3] = p1 + p2
            ip += 4
        elif opcode == 2:  # multiply
            p1, p2, p3 = get_params(3)
            intcode[p3] = p1 * p2
            ip += 4
        elif opcode == 3:  # input
            p1, = get_params(1)
            intcode[p1] = 1  # int(input("Enter integer input: "))
            ip += 2
        elif opcode == 4:  # print
            p1, = get_params(1)
            yield p1
            ip += 2
        elif opcode == 5:  # jump-if-true
            p1, p2 = get_params(2)
            if p1 != 0:
                ip = p2
            else:
                ip += 3
        elif opcode == 6:  # jump-if-false
            p1, p2 = get_params(2)
            if p1 == 0:
                ip = p2
            else:
                ip += 3
        elif opcode == 7:  # less than
            p1, p2, p3 = get_params(3)
            if p1 < p2:
                intcode[p3] = 1
            else:
                intcode[p3] = 0
            ip += 4
        elif opcode == 8:  # equals
            p1, p2, p3 = get_params(3)
            if p1 == p2:
                intcode[p3] = 1
            else:
                intcode[p3] = 0
            ip += 4
        else:
            raise ValueError
