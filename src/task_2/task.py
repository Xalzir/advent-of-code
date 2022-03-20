# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    position = 0
    depth = 0

    for line in input.splitlines():
        direction, amount = line.split()
        amount = int(amount)
        match direction:
            case "up":
                depth -= amount
            case "down":
                depth += amount
            case "forward":
                position += amount

    return position * depth


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    aim = 0
    position = 0
    depth = 0

    for line in input.splitlines():
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

    return position * depth
