from collections import defaultdict


def get_input() -> list[str]:
    with open("input.txt") as data:
        return data.read().splitlines()


input = get_input()
input_num_lenght = len(input[0])

# **************************************** PART ONE ****************************************
column_bit_counter: dict[int, int] = defaultdict(int)
for line in input:
    for i, bit in enumerate(line):
        if bit == "1":
            column_bit_counter[i] += 1

num_1 = 0
num_2 = 0
for i in range(input_num_lenght):
    if column_bit_counter[i] > len(input) / 2:
        num_1 += 2 ** (input_num_lenght - i - 1)
    else:
        num_2 += 2 ** (input_num_lenght - i - 1)

print(f"result for first subtask: {num_1*num_2}")

# **************************************** PART TWO ****************************************
def get_rating(searched_bit_1: str, searched_bit_2: str) -> int:
    input_tmp = input.copy()
    for i in range(input_num_lenght):
        if len(input_tmp) == 1:
            break
        column_bit_sum = sum(line[i] == "1" for line in input_tmp)
        if column_bit_sum >= len(input_tmp) / 2:
            input_tmp = [line for line in input_tmp if line[i] != searched_bit_1]
        else:
            input_tmp = [line for line in input_tmp if line[i] != searched_bit_2]
    return int(input_tmp[0], 2)


num_1 = get_rating("0", "1")
num_2 = get_rating("1", "0")

print(f"result for second subtask: {num_1 * num_2}")
