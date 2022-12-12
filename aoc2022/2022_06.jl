open("data/day_06.txt", "r") do f
    datastream = read(f, String)
    for (part, marker_length) in enumerate([4, 14])
        for idx in marker_length:length(datastream)
            # get whole marker, convert it to set
            marker = Set(split(SubString(datastream, idx - marker_length + 1, idx), ""))
            if length(marker) == marker_length
                println("Day 6 - part $part: ", idx)
                break
            end
        end
    end
end
