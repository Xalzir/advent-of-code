def get_input():
    with open("input.txt") as data:
        return data.read().splitlines()


input = get_input()

# **************************************** PART ONE ****************************************
position = 0
depth = 0

for line in input:
    direction, amount = line.split()
    amount = int(amount)
    match direction:
        case "up":
            depth -= amount
        case "down":
            depth += amount
        case "forward":
            position += amount

print(f"result for first subtask: {position*depth}")

# **************************************** PART TWO ****************************************
aim = 0
position = 0
depth = 0

for line in input:
    direction, amount = line.split()
    amount = int(amount)
    match direction:
        case "up":
            aim -= amount
        case "down":
            aim += amount
        case "forward":
            position += amount
            depth += aim * amount

print(f"result for second subtask: {position*depth}")
