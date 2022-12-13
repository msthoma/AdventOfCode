import DataStructures: OrderedDict

re = r"Monkey (\d+?):.+?items: ([\d, ]+?) Operation.+ old (.+?) Test: divisible by (\d+).+monkey (\d+).+monkey (\d+)"

function parse_operation(op::AbstractString)
    operator, val = split(op)

    if operator == "+"
        o = +
    elseif operator == "*"
        o = *
    else
        error
    end

    if val == "old"
        return x -> o(x, x)
    else
        return x -> o(x, parse(Int, val))
    end
end

for part in [1, 2]
    n_rounds = part == 1 ? 20 : 10000

    open("data/day_11.txt", "r") do f
        monkeys = OrderedDict()

        for instructions in split(read(f, String), "\n\n")
            m = match(re, replace(instructions, "\n" => ""))
            monkey, items, operation, divisible_by, monkey_if_true, monkey_if_false = m

            monkeys[parse(Int, monkey)] = Dict(
                "items" => parse.(BigInt, split(items, ", ")),
                "operation" => parse_operation(operation),
                "divisible_by" => parse(Int, divisible_by),
                "monkey_if_true" => parse(Int, monkey_if_true),
                "monkey_if_false" => parse(Int, monkey_if_false),
                "total_inspections" => 0,
            )
        end

        # trick to find part 2 solution, taken from here https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/izrd7iz/
        # more detailed explanation here https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/izsce95/
        modulo_part_2 = *([v["divisible_by"] for (_, v) in monkeys]...)

        for r in 1:n_rounds
            for (monkey, notes) in monkeys
                items = notes["items"]

                while length(items) > 0
                    # monkey inspects
                    item_worry = popfirst!(items)
                    notes["total_inspections"] += 1

                    # apply operation
                    item_worry = notes["operation"](item_worry)

                    if part == 1
                        # monkey gets bored
                        item_worry = item_worry ÷ 3
                    elseif part == 2
                        item_worry = item_worry % modulo_part_2
                    else
                        error
                    end

                    # find which monkey to throw to
                    monkey_to_throw_to = item_worry % notes["divisible_by"] == 0 ? notes["monkey_if_true"] : notes["monkey_if_false"]

                    # throw
                    push!(monkeys[monkey_to_throw_to]["items"], item_worry)
                end
            end
        end

        println("Day 11 - part $part: ", *(sort([v["total_inspections"] for (_, v) in monkeys])[end-1:end]...))
    end
end