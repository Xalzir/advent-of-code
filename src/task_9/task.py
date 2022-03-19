from typing import Iterator


def get_input() -> list[str]:
    with open("input.txt") as data:
        return [line for line in data.read().splitlines()]


input = get_input()


def adjacent_cords(x: int, y: int) -> Iterator[tuple[int, int]]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


# **************************************** PART ONE ****************************************
def all_adjacent_cords_are_lower(x: int, y: int, coord_value: int) -> bool:
    return all(coords.get(pt, 9) > coord_value for pt in adjacent_cords(x, y))


coords = {(x, y): int(num) for y, line in enumerate(input) for x, num in enumerate(line)}
low_points = [((x, y), num) for (x, y), num in coords.items() if all_adjacent_cords_are_lower(x, y, num)]
first_result = sum(num + 1 for *_, num in low_points)

print(f"Result for first subtask: {first_result}")

# **************************************** PART TWO ****************************************
basins = []

for (x, y), _ in low_points:
    checked = set()
    to_check = [(x, y)]

    while to_check:
        x, y = to_check.pop()
        checked.add((x, y))

        for point in adjacent_cords(x, y):
            if point not in checked and coords.get(point, 9) != 9:
                to_check.append(point)

    basins.append(len(checked))

basins.sort()
second_result = basins[-1] * basins[-2] * basins[-3]

print(f"Result for second subtask: {second_result}")
