# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    parsed_input = [int(line) for line in input.splitlines()]
    result = sum(parsed_input[i] > parsed_input[i - 1] for i in range(1, len(parsed_input)))
    return result


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    parsed_input = [int(line) for line in input.splitlines()]
    result = sum(parsed_input[i] > parsed_input[i - 3] for i in range(3, len(parsed_input)))
    return result
