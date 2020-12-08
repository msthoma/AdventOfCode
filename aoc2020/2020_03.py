from utils import utils


def count_trees(right, down, grid):
    overall_x = -right  # start at minus right so the 1st square is at [0,0]
    row_length = len(grid[0])
    tree_count = 0
    for y, row in enumerate(grid):
        if y % down == 0:
            overall_x += right
            local_x = overall_x % row_length
            if row[local_x] == "#":
                tree_count += 1
    return tree_count


def main():
    # import/process day data
    data = utils.data(2020, 3).splitlines()

    # part a
    answer_a = count_trees(3, 1, data)
    print("Answer part a:", answer_a)

    # part b
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (right, down)
    answer_b = 1
    for slope in slopes:
        answer_b *= count_trees(*slope, data)
    print("Answer part b:", answer_b)


if __name__ == '__main__':
    main()
