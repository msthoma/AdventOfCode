def computer(intcode, input_list, ip=0, feedback=False, extend=False):
    input_list = iter(input_list)

    base = 0

    if extend:
        intcode.extend([0] * 10000)

    valid_opcodes = list(range(1, 10))
    valid_opcodes.append(99)

    def get_params(nparams):
        op_str = str(intcode[ip])
        op = int(op_str[-2:])

        # get modes
        modes = [0] * 3
        if len(op_str) != 1:
            for i, mode in enumerate(op_str[:-2][::-1]):
                mode = int(mode)
                assert mode in [0, 1, 2]
                modes[i] = mode

        # get params
        params = []
        for i in range(1, nparams + 1):
            param = intcode[ip + i]  # immediate case
            mode = modes[i - 1]
            if i < nparams or op not in [1, 2, 3, 7, 8]:
                if mode == 0:
                    param = intcode[param]  # position case
                elif mode == 2:
                    param = intcode[param + base]  # relative case
            elif mode == 2:
                param += base  # relative case
            params.append(param)
        return params

    res = {"output": [], "ip": ip, "halt": False}

    while True:
        opcode = int(str(intcode[ip])[-2:])
        assert opcode in valid_opcodes

        if opcode == 99:  # terminate
            res["halt"] = True
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
            intcode[p1] = next(input_list)
            ip += 2
        elif opcode == 4:  # print
            p1, = get_params(1)
            ip += 2
            res["output"].append(p1)
            res["ip"] = ip
            if feedback:
                break
        elif opcode == 5:  # jump-if-true
            p1, p2 = get_params(2)
            if p1:
                ip = p2
            else:
                ip += 3
        elif opcode == 6:  # jump-if-false
            p1, p2 = get_params(2)
            if not p1:
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
        elif opcode == 9:
            p1, = get_params(1)
            base += p1
            ip += 2
        else:
            raise ValueError

    return res
