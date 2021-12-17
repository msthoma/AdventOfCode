from utils.utils import get_data, res_print2

if __name__ == '__main__':
    data = get_data().splitlines()
    gamma = list(map(lambda y: y > len(data) / 2, map(lambda x: x.count('1'), zip(*data))))
    epsilon = [str(int(not x)) for x in gamma]
    gamma = list(map(str, map(int, gamma)))

    o2_co2 = []
    for criteria in ["1", "0"]:
        rating = data.copy()
        for i in range(len(data[0])):
            all_at_i = [x[i] for x in rating]
            count_1, count_0 = all_at_i.count("1"), all_at_i.count("0")

            if count_1 == count_0:
                rating = list(filter(lambda x: x[i] == criteria, rating))
            elif count_1 > count_0:
                rating = list(filter(lambda x: x[i] == criteria, rating))
            else:
                other = "0" if criteria == "1" else "1"
                rating = list(filter(lambda x: x[i] == other, rating))

            if len(rating) == 1:
                break
        o2_co2.append(rating[0])

    res_print2(int("".join(gamma), 2) * int("".join(epsilon), 2), 1)
    res_print2(int(o2_co2[0], 2) * int(o2_co2[1], 2), 2)
