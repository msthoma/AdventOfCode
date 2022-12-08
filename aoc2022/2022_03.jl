import IterTools

priorities = Dict(j => i for (i, j) in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

open("data/day_03.txt", "r") do f
    lines = readlines(f)

    priorities_part_1 = Int[]

    for line in lines
        halfway = length(line) ÷ 2
        common_items = intersect(Set(line[1:halfway]), Set(line[halfway+1:end]))
        # there should be only one common item, but iterate through the intersection anyway
        for item in common_items
            push!(priorities_part_1, priorities[item])
        end
    end


    priorities_part_2 = Int[]
    for line_group in IterTools.partition(lines, 3)
        badge = intersect([Set(l) for l in line_group]...)
        # there should be only one badge, but iterate through the intersection anyway
        for b in badge
            push!(priorities_part_2, priorities[b])
        end
    end

    println("Day 3 - part 1: ", sum(priorities_part_1))
    println("Day 3 - part 2: ", sum(priorities_part_2))
end
