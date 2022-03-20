class Board:
    def __init__(self, unparsed_board):
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


def prepare_inputs_and_boards(input: str) -> tuple[list[int], list[Board]]:
    numbers, *unparsed_boards = input.split("\n\n")
    input_numbers = [int(num) for num in numbers.split(",")]
    boards = [Board(unparsed_board) for unparsed_board in unparsed_boards]
    return input_numbers, boards


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    input_numbers, boards = prepare_inputs_and_boards(input)
    for number in input_numbers:
        for board in boards:
            board.left_nums.discard(number)
            if board.has_won:
                return sum(board.left_nums) * number


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    input_numbers, boards = prepare_inputs_and_boards(input)
    last_winner = 0

    for number in input_numbers:
        for board in [board for board in boards if not board.has_won]:
            board.left_nums.discard(number)
            if board.has_won:
                last_winner = sum(board.left_nums) * number
    return last_winner
