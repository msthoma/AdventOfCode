import pandas as pd
from matplotlib import pyplot as plt

from utils.utils import day_name, input_fp, print_res


def gen_point_path(directions):
    path = [[0, 0]]
    for direction in directions:
        d = direction[0]
        steps = int(direction[1:])

        if d in ["R", "L"]:
            sign = 1 * -1 if d == "L" else 1
            x, y = path[-1]
            for i in range(1, steps + 1):
                path.append([x + sign * i, y])

        elif d in ["U", "D"]:
            sign = 1 * -1 if d == "D" else 1
            x, y = path[-1]
            for i in range(1, steps + 1):
                path.append([x, y + sign * i])
    return path


def main():
    day = day_name()
    with open(input_fp(day), "r") as f:
        input_data = f.read()
    first, second = input_data.splitlines()

    first = first.split(sep=",")
    second = second.split(sep=",")

    first_path = gen_point_path(first)
    second_path = gen_point_path(second)

    df_first = pd.DataFrame(first_path, columns=["x1", "y1"])
    df_first["x1y1"] = df_first["x1"].astype(str).str.cat(df_first["y1"].astype(str), sep="x")

    df_second = pd.DataFrame(second_path, columns=["x2", "y2"])
    df_second["x2y2"] = df_second["x2"].astype(str).str.cat(df_second["y2"].astype(str), sep="x")

    common = pd.merge(df_first, df_second, how="inner", left_on="x1y1", right_on="x2y2")
    common["manhattan"] = abs(common["x1"]) + abs(common["y1"])

    print_res(day, 1, common.loc[1:, "manhattan"].min())

    sums = [df_first[df_first["x1y1"] == inter].index.values.astype(int)[0] +
            df_second[df_second["x2y2"] == inter].index.values.astype(int)[0] for inter in common.loc[1:, "x1y1"]]

    print_res(day, 2, min(sums))

    # optionally plot paths
    # plt.scatter(df_first.loc[:, "x1"], df_first.loc[:, "y1"], s=1, c="red")
    # plt.scatter(df_second.loc[:, "x2"], df_second.loc[:, "y2"], s=1)
    # plt.show()


if __name__ == '__main__':
    main()
