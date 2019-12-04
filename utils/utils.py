import os
import sys


def get_day_name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]
