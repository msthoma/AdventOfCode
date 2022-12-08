open("day04_input.txt", "r") do f
    lines = readlines(f)

    fully_contained = 0
    overlap = 0

    for line in lines
        # parse line into two arrays of 2 integers
        l = [parse.(Int, split(r, "-")) for r in split(line, ",")]
        # convert them to ranges, then sets
        r1, r2 = map(x -> Set(range(x...)), l)

        if issubset(r1, r2) || issubset(r2, r1)
            fully_contained += 1
        end

        if length(intersect(r1, r2)) != 0
            overlap += 1
        end
    end

    println("Day 4 - part 1: ", fully_contained)
    println("Day 4 - part 1: ", overlap)
end
