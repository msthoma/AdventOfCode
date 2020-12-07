import numpy as np

from utils import utils


def sum3(data, goal_sum=2020):
    # implemented from https://en.wikipedia.org/wiki/3SUM#Quadratic_algorithm
    data = sorted(data)
    for i in range(len(data) - 2):
        a = data[i]
        start = i + 1
        end = len(data) - 1
        while start < end:
            b = data[start]
            c = data[end]
            if sum([a, b, c]) == goal_sum:
                return [a, b, c]
            elif sum([a, b, c]) > goal_sum:
                end -= 1
            else:
                start += 1


def main():
    data = sorted(int(i) for i in utils.data(2020, 1).splitlines())
    data_desc = sorted(data, reverse=True)

    # part a
    for i in data:
        for j in data_desc:
            if i + j == 2020:
                print("Answer part a:", [i, j], "product:", i * j)
                break
        else:
            continue
        break

    # part b
    data2 = np.array(data)
    # numbers larger than 2020 - (sum of two smallest numbers) can be excluded
    data2 = data2[data2 <= (2020 - data2[:2].sum())]

    answer_b = sum3(data2)
    print("Answer part b:", answer_b, "product:", np.prod(answer_b))


if __name__ == '__main__':
    main()
