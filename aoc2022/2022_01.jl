open("data/day_01.txt", "r") do f
    data = sort([sum(parse.(Int, split(line))) for line in split(read(f, String), "\n\n")], rev=true)
    println("Day 1 - part 1: ", max(data...))
    println("Day 1 - part 2: ", sum(data[1:3]))
end
