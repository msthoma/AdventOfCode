import networkx as nx
from utils.utils import get_script_file_name, input_fp, res_print


def main():
    day = get_script_file_name()
    with open(input_fp(day), "r") as f:
        input_data = [line.strip().split(")") for line in f.read().splitlines()]

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

    res_print(day, 1, sum(get_path(obj) for obj in all_objects))

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
    res_print(day, 2, distance)

    # alternative solution with networkx
    g = nx.DiGraph()
    for pair in input_data:
        g.add_edge(*pair)
    res_print(day, 1, nx.transitive_closure(g).size())
    res_print(day, 2, nx.shortest_path_length(g.to_undirected(), "YOU", "SAN") - 2)


if __name__ == '__main__':
    main()
