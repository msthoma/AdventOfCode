def computer(intcode):
    ip = 0
    opcode = intcode[ip]

    def get_params(nparams):
        # extract opcode
        opcode_str = str(intcode[ip])
        opcode = int(opcode_str[-2])
        assert opcode in range(1, 9)

        # get modes
        modes = [0] * nparams
        if len(opcode_str) != 1:
            for i, mode in enumerate(opcode_str[:-2][::-1]):
                mode = int(mode)
                assert mode in [0, 1]
                modes[i] = mode

        # get params
        params = []
        for i in range(1, nparams + 1):
            param = intcode[ip + i]  # immediate case
            if modes[i] == 0 and i < nparams:
                param = intcode[param]  # position case
            params.append(param)

        return params

    while True:
        if opcode == 99:  # terminate
            return intcode
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
            intcode[p1] = int(input("Enter integer input: "))
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
            pass
