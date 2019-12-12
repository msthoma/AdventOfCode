from utils.utils import get_day_name, get_input_fp, print_res


def main():
    day = get_day_name()
    with open(get_input_fp(day), "r") as f:
        input_data = [line.split(")") for line in f.read().splitlines()]

    # get all objects
    all_objects = set(val for pair in input_data for val in pair)

    # get parent of each object
    object_parents = {k: v for v, k in input_data}

    # calculate path length for each object recursively
    path_lengths = {}

    def get_path(obj):
        if obj not in path_lengths:
            if obj in object_parents:
                path_lengths[obj] = 1 + get_path(object_parents[obj])
            else:
                path_lengths[obj] = 0
        return path_lengths[obj]

    print_res(day, 1, sum(get_path(obj) for obj in all_objects))

    # path from SAN to COM
    san_to_com = ["SAN"]
    while san_to_com[-1] in object_parents:
        san_to_com.append(object_parents[san_to_com[-1]])
    # path from me to COM
    me_to_com = ["YOU"]
    while me_to_com[-1] in object_parents:
        me_to_com.append(object_parents[me_to_com[-1]])

    # find least common ancestor and sum distances from it
    distance = 0
    for obj in me_to_com:
        if obj in san_to_com:
            distance = me_to_com.index(obj) + san_to_com.index(obj)
            distance = distance - 2  # exclude YOU and SAN
            break
    print_res(day, 2, distance)


if __name__ == '__main__':
    main()
