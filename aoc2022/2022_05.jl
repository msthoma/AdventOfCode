import DataStructures: DefaultDict, OrderedDict

open("data/day_05.txt", "r") do f
    stacks, moves = split(read(f, String), "\n\n")

    # parse stacks into a DefaultDict
    dd = DefaultDict{Int,Vector{String}}(Vector{String})

    for line in split(stacks, "\n")
        m = Dict(x.offset => x.match for x in eachmatch(r"[A-Z]", line))
        for m in eachmatch(r"[A-Z]", line)
            push!(dd[m.offset], m.match)
        end
    end

    stacks_ordered_part_1 = OrderedDict{Int,Vector{String}}()

    # sort DefaultDict, and replace the indices of the matches with the numbers 1-9
    for (i, j) in enumerate(sort(collect(dd), by=x -> x[1]))
        old_idx, stack = j
        # important to reverse the stacks here, since they are parsed in reversed order
        stacks_ordered_part_1[i] = reverse(stack)
    end

    stacks_ordered_part_2 = deepcopy(stacks_ordered_part_1)

    # follow all the moves
    for move in split(moves, "\n", keepempty=false)
        a = match(r"move (\d+) from (\d+) to (\d+)", move).captures
        n, from, to = parse.(Int, a)

        # part 1
        for _ in range(1, n)
            to_move = pop!(stacks_ordered_part_1[from])
            push!(stacks_ordered_part_1[to], to_move)
        end

        # part 2
        to_move_all = stacks_ordered_part_2[from][end-n+1:end]
        remaining = stacks_ordered_part_2[from][1:end-n]
        append!(stacks_ordered_part_2[to], to_move_all)
        stacks_ordered_part_2[from] = remaining
    end

    println("Day 5 - part 1: ", join([last(v) for (k, v) in stacks_ordered_part_1]))
    println("Day 5 - part 2: ", join([last(v) for (k, v) in stacks_ordered_part_2]))
end
