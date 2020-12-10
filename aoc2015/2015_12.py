import json
import re

from utils.utils import get_data, res_print2


def sum_no_red(obj):
    if type(obj) is int:
        return obj
    elif type(obj) is dict:
        if "red" in obj.values():
            return 0
        else:
            return sum(sum_no_red(v) for v in obj.values())
    elif type(obj) is list:
        return sum(sum_no_red(v) for v in obj)
    else:
        return 0


def json_hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj


def main():
    data = get_data()

    # part a
    pat = re.compile(r"-*\d+")
    res_print2(sum(map(int, pat.findall(data))), 1)

    # part b 1st method
    res_print2(sum_no_red(json.loads(data)), 2)

    # part b 2nd method
    data = str(json.loads(data, object_hook=json_hook))
    res_print2(sum(map(int, pat.findall(data))), 2)


if __name__ == '__main__':
    main()
