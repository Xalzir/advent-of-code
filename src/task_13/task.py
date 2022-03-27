def prepare_input(input: str) -> tuple[set[tuple[int, int]], list[str]]:
    points, instructions = input.split("\n\n")
    return {(int(x), int(y)) for x, y in [line.split(",") for line in points.splitlines()]}, instructions.splitlines()


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    points, instructions = prepare_input(input)

    for instruction in instructions:
        instruction, num = instruction.split("=")
        num = int(num)

        if instruction[-1] == "x":
            points = {(x if x < num else 2 * num - x, y) for x, y in points}
        else:
            points = {(x, y if y < num else 2 * num - y) for x, y in points}
        break
    return len(points)


# **************************************** PART TWO ****************************************
def stringified_points(points) -> None:
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    res_string = ""
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in points:
                res_string += "@"
            else:
                res_string += " "
        res_string += "\n"
    return res_string


def second_subtask(input: str) -> int:
    points, instructions = prepare_input(input)

    for instruction in instructions:
        instruction, num = instruction.split("=")
        num = int(num)

        if instruction[-1] == "x":
            points = {(x if x < num else 2 * num - x, y) for x, y in points}
        else:
            points = {(x, y if y < num else 2 * num - y) for x, y in points}
    return stringified_points(points)
