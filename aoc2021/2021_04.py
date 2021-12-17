import numpy as np

from utils.utils import get_data, res_print2


class Board(object):

    def __init__(self, numbers: str) -> None:
        numbers = [list(map(int, n.strip().replace("  ", " ").split(" "))) for n in numbers.split("\n")]
        self.grid = np.array(numbers)
        self.state = np.zeros((5, 5), dtype=int)
        super().__init__()

    def mark_number(self, number: int):
        self.state[np.where(self.grid == number)] = 1

    def has_winning(self):
        return (self.state.all(axis=0)).any() or (self.state.all(axis=1)).any()

    def sum_of_unmarked(self):
        return np.multiply(self.grid, 1 - self.state).sum()


if __name__ == '__main__':
    data = get_data().split("\n\n")
    boards = [Board(numbers=b) for b in data[1:]]
    first_winner, last_winner = None, None

    for i in map(int, data[0].split(",")):
        for board in boards:
            board.mark_number(i)
            if first_winner is None:
                if board.has_winning():
                    first_winner = board
                    res_print2(i * board.sum_of_unmarked(), 1)
            if all(b.has_winning() for b in boards):
                last_winner = board
                res_print2(i * board.sum_of_unmarked(), 2)
                break
        if last_winner is not None:
            break
