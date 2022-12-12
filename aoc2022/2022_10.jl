open("data/day_10.txt", "r") do f
    cycles = Int[1]
    for signal in readlines(f)
        if signal == "noop"
            push!(cycles, 0)
        elseif startswith(signal, "addx")
            _, val = split(signal)
            push!(cycles, 0, parse(Int, val))
        else
            error
        end
    end

    part_1 = 0
    for c in 20:40:220
        part_1 += sum(cycles[1:c]) * c
    end

    println("Day 10 - part 1: ", part_1)

    println("Day 10 - part 2: ")

    part_2 = [(i - 1) % 40 in range(p - 1, p + 1) ? "#" : "." for (i, p) in enumerate(cumsum(cycles))]
    for c in 40:40:240
        println(join(part_2[c-40+1:c]))
    end

end
