from collections import defaultdict

from tqdm import tqdm

from utils.utils import get_data, res_print2


def main():
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split(
        "\n\n"
    )
    data: list[str] = get_data().split("\n\n")

    seeds_part_a, *maps_str = data
    seeds_part_a = list(
        map(int, seeds_part_a.lstrip("seeds: ").split(" "))
    )  #*23423432

    # 86860277
    # print(seeds*868607)
    print(len(seeds_part_a))

    # part_a, part_b = {}, {}

    maps: dict[str, list[tuple[int, int, int]]] = {}

    for m in maps_str:
        map_type, *ranges_str = m.splitlines()
        map_type = map_type.rstrip(" map:")
        # print(map_type, ranges)
        parsed_ranges = []
        for r in ranges_str:
            dest_start, src_start, length = map(int, r.split(" "))
            # parsed_ranges.append((range(src_start, src_start + length), dest_start))
            parsed_ranges.append((src_start, src_start + length, dest_start))
        maps[map_type] = sorted(parsed_ranges)
        print(map_type, parsed_ranges)

    min_location = -1
    for seed in tqdm(seeds_part_a):
        current = seed
        for category_map, ranges in maps.items():
            to = current
            for src_start, src_end, dest_start in ranges:
                if current >= src_start and current < src_end:
                    to = dest_start + current - src_start
                    break

            current = to
        if min_location == -1:
            min_location = current
        else:
            min_location = current if min_location > current else min_location

    res_print2(min_location, part=1)

    print(sum(seeds_part_a[1::2]) / 20)


if __name__ == "__main__":
    main()
