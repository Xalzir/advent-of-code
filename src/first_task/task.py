def get_input():
    with open("input.txt") as data:
        return [int(line) for line in data.read().splitlines()]


input = get_input()

# **************************************** PART ONE ****************************************
first_result = sum(input[i] > input[i - 1] for i in range(1, len(input)))
print(f"Result for first subtask: {first_result}")

# **************************************** PART TWO ****************************************
second_result = sum(input[i] > input[i - 3] for i in range(3, len(input)))
print(f"Result for second subtask: {second_result}")
