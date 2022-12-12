import DataStructures: OrderedDict

abs_sum(x) = sum(abs.(x))

open("data/day_09.txt", "r") do f
    # possible movements for head knot
    movements = Dict{String,Vector{Int}}("U" => [1, 0], "D" => [-1, 0], "L" => [0, -1], "R" => [0, 1])

    # these are the routes for all knots: H, 1, 2, ..., 9
    all_routes = OrderedDict{Int,Vector{Vector{Int}}}(pos => [[0, 0]] for pos in 0:9)

    for line in readlines(f)
        m = match(r"([A-Z]{1}) (\d+)", line)
        direction = m.captures[1]
        distance = parse(Int, m.captures[2])

        for _ in 1:distance
            # move the head knot first
            head_position = last(all_routes[0])
            head_position += movements[direction]
            push!(all_routes[0], head_position)

            # and then iterate over all subsequent knots and move them accordingly
            for part in 1:9
                new_head_position = last(all_routes[part-1])
                tail_position = last(all_routes[part])

                # this determines how much to move a knot
                d = new_head_position - tail_position
                if abs_sum(d) <= 2
                    tail_change = (new_head_position - tail_position) .÷ 2
                else
                    tail_change = [abs(p) == 2 ? p ÷ 2 : p for p in d]
                end

                push!(all_routes[part], tail_position + tail_change)
            end
        end
    end

    println("Day 9 - part 1: ", length(Set(all_routes[1])))
    println("Day 9 - part 2: ", length(Set(all_routes[9])))
end
