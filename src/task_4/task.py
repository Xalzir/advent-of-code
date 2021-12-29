def get_input() -> list[str]:
    with open("input.txt") as data:
        return data.read().split("\n\n")


numbers, *unparsed_boards = get_input()


class Board:
    def __init__(self, unparsed_board) -> None:
        self.board = [[int(num) for num in line.split()] for line in unparsed_board.splitlines()]
        self.left_nums = {int(num) for num in unparsed_board.split()}

    @property
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.board[i][j] in self.left_nums:
                    break
            else:
                return True
            for j in range(5):
                if self.board[j][i] in self.left_nums:
                    break
            else:
                return True
        return False


input_numbers = [int(num) for num in numbers.split(",")]

# **************************************** PART ONE ****************************************
boards = [Board(unparsed_board) for unparsed_board in unparsed_boards]


def get_first_subtask_result() -> int:
    for number in input_numbers:
        for board in boards:
            board.left_nums.discard(number)
            if board.has_won:
                return sum(board.left_nums) * number


print(f"result for first subtask: {get_first_subtask_result()}")

# **************************************** PART TWO ****************************************
boards = [Board(unparsed_board) for unparsed_board in unparsed_boards]
last_winner = 0

for number in input_numbers:
    for board in [board for board in boards if not board.has_won]:
        board.left_nums.discard(number)
        if board.has_won:
            last_winner = sum(board.left_nums) * number

print(f"result for first subtask: {last_winner}")
