from collections import Counter


def get_input() -> str:
    with open("input.txt") as data:
        return data.read()


input = get_input()


def get_num_of_fishes(num_of_days: int) -> int:
    numbers_count = Counter(int(num) for num in input.strip().split(","))
    for _ in range(num_of_days):
        tmp_count = Counter({6: numbers_count[0], 8: numbers_count[0]})
        tmp_count.update({number - 1: count for number, count in numbers_count.items() if number != 0})
        numbers_count = tmp_count
    return sum(numbers_count.values())


# **************************************** PART ONE ****************************************
print(f"result for first subtask: {get_num_of_fishes(80)}")

# **************************************** PART TWO ****************************************
print(f"result for second subtask: {get_num_of_fishes(256)}")
