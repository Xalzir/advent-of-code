def get_input() -> str:
    with open("input.txt") as data:
        return data.read()


input = [int(num) for num in get_input().strip().split(",")]

# **************************************** PART ONE ****************************************
res = min(sum(abs(number - position) for number in input) for position in range(min(input), max(input) + 1))

print(f"result for first subtask: {res}")

# **************************************** PART TWO ****************************************
res = min(
    sum(abs(number - position) * (abs(number - position) + 1) // 2 for number in input)
    for position in range(min(input), max(input) + 1)
)

print(f"result for second subtask: {res}")
