import hashlib

from utils.utils import get_data, res_print2


def main():
    data = get_data()

    i = 1
    while True:
        md5 = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        if md5.startswith("00000"):
            res_print2((i, md5), 1)
            break
        i += 1

    i = 1
    while True:
        md5 = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        if md5.startswith("000000"):
            res_print2((i, md5), 2)
            break
        i += 1


if __name__ == '__main__':
    main()
