import re

import numpy as np

from utils.utils import res_print2, get_data

if __name__ == '__main__':
    data = get_data().splitlines()

    closing_chars = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total_syntax_error, autocomplete_scores = 0, []
    pair_pattern = re.compile(r"\(\)|\[]|{}|<>")
    opening_char_pattern = re.compile(r"[(\[{<]")
    opening_closing_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_table = {v: i for i, v in enumerate(opening_closing_chars.values(), start=1)}
    for line in data:
        while pair_pattern.search(line) is not None:
            line = pair_pattern.sub("", line)
        if any(char in line for char in closing_chars.keys()):
            # part 1
            line = opening_char_pattern.sub("", line)
            total_syntax_error += closing_chars[line[0]]
        else:
            # part 2
            for opening_char in opening_closing_chars.keys():
                line = line.replace(opening_char, opening_closing_chars[opening_char])
            completion_score = 0
            for closing_char in reversed(line):
                completion_score *= 5
                completion_score += score_table[closing_char]
            autocomplete_scores.append(completion_score)

    res_print2(total_syntax_error, 1)
    res_print2(int(np.median(autocomplete_scores)), 2)
