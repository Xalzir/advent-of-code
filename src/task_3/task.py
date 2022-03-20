from collections import defaultdict


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    parsed_input = input.splitlines()
    input_num_lenght = len(parsed_input[0])
    column_bit_counter: dict[int, int] = defaultdict(int)
    for line in parsed_input:
        for i, bit in enumerate(line):
            if bit == "1":
                column_bit_counter[i] += 1

    num_1 = 0
    num_2 = 0
    for i in range(input_num_lenght):
        if column_bit_counter[i] > len(parsed_input) / 2:
            num_1 += 2 ** (input_num_lenght - i - 1)
        else:
            num_2 += 2 ** (input_num_lenght - i - 1)

    return num_1 * num_2


# **************************************** PART TWO ****************************************
def get_rating(input: str, searched_bit_1: str, searched_bit_2: str) -> int:
    parsed_input = input.splitlines()
    input_num_lenght = len(parsed_input[0])
    input_tmp = parsed_input.copy()
    for i in range(input_num_lenght):
        if len(input_tmp) == 1:
            break
        column_bit_sum = sum(line[i] == "1" for line in input_tmp)
        if column_bit_sum >= len(input_tmp) / 2:
            input_tmp = [line for line in input_tmp if line[i] != searched_bit_1]
        else:
            input_tmp = [line for line in input_tmp if line[i] != searched_bit_2]
    return int(input_tmp[0], 2)


def second_subtask(input: str) -> int:
    return get_rating(input, "0", "1") * get_rating(input, "1", "0")
