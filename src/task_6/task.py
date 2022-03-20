from collections import Counter


def get_num_of_fishes(num_of_days: int, input: str) -> int:
    numbers_count = Counter(int(num) for num in input.strip().split(","))
    for _ in range(num_of_days):
        tmp_count = Counter({6: numbers_count[0], 8: numbers_count[0]})
        tmp_count.update({number - 1: count for number, count in numbers_count.items() if number != 0})
        numbers_count = tmp_count
    return sum(numbers_count.values())


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    return get_num_of_fishes(80, input)


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    return get_num_of_fishes(256, input)
