import more_itertools

from utils.utils import get_data

if __name__ == '__main__':
    data = list(map(int, get_data(2021, 1).splitlines()))
    increases = 0
    for i, val in enumerate(data[1:], start=1):
        if val > data[i - 1]:
            increases += 1
    print("Answer part a:", increases)

    data_2 = [sum(win) for win in more_itertools.windowed(data, 3)]
    increases_2 = 0
    for i, val in enumerate(data_2[1:], start=1):
        if val > data_2[i - 1]:
            increases_2 += 1

    print("Answer part a:", increases_2)
