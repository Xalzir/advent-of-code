# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    input = [int(num) for num in input.strip().split(",")]
    return min(sum(abs(number - position) for number in input) for position in range(min(input), max(input) + 1))


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    input = [int(num) for num in input.strip().split(",")]
    return min(
        sum(abs(number - position) * (abs(number - position) + 1) // 2 for number in input)
        for position in range(min(input), max(input) + 1)
    )
