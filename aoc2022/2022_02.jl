# part 1
# A for Rock, B for Paper, C for Scissors
# X for Rock, Y for Paper, Z for Scissors

# lose 0, draw 3, win 6
draw = ["AX", "BY", "CZ"]
win = ["AY", "BZ", "CX"]
lose = ["AZ", "BX", "CY"]

shape_scores = Dict{String,Int}("X" => 1, "Y" => 2, "Z" => 3)

# part 2
# X means you need to lose, Y means you need to draw, Z means you need to win

open("day02_input.txt", "r") do f
    data = [split(line, " ") for line in readlines(f)]

    total_score = 0
    for (i, j) in data
        shape_score = shape_scores[j]

        comb = i * j
        if comb in lose
            w = 0
        elseif comb in draw
            w = 3
        elseif comb in win
            w = 6
        else
            error("unexpected combination")
        end
        total_score += (w + shape_score)
    end
    println("Day 2 - part 1: ", total_score)
end
