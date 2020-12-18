from utils.utils import get_data, res_print2


def main():
    data = get_data()

    earliest, buses = data.splitlines()
    earliest = int(earliest)
    all_buses = buses.split(",")

    # part a
    buses = [int(b) for b in all_buses if b.isdigit()]
    times_to_closest = [bus - (earliest % bus) for bus in buses]
    closest = min(times_to_closest)
    closest_bus = buses[times_to_closest.index(closest)]
    res_print2(closest * closest_bus, 1)

    # part b
    max_interval_bus = max(buses)
    start_at = (100000000000000 // max_interval_bus) * max_interval_bus

    offsets = [all_buses.index(str(b)) for b in buses]
    print(all_buses)
    print(offsets[buses.index(max_interval_bus)])
    offsets_of_max = [o - offsets[buses.index(max_interval_bus)] for o in
                      offsets]
    print(offsets)
    print(offsets_of_max)
    print(earliest, buses, max_interval_bus, start_at)

    # current = start_at
    # print(current)
    # i = 0
    # while True:
    #     i += 1
    #     current += max_interval_bus
    #     if i % 10000 == 0:
    #         print(current)
    #
    #     if any((current + o) % b != 0 for o, b in zip(offsets_of_max, buses)):
    #         continue
    #     else:
    #         break
    #
    # res_print2(current - offsets_of_max[0], 2)


if __name__ == '__main__':
    main()
