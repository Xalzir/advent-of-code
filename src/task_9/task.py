from typing import Iterator


def adjacent_cords(x: int, y: int) -> Iterator[tuple[int, int]]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def all_adjacent_cords_are_lower(x: int, y: int, coord_value: int, coords) -> bool:
    return all(coords.get(pt, 9) > coord_value for pt in adjacent_cords(x, y))


def prepare_coords_dict(input: str) -> dict[tuple[int, int], int]:
    return {(x, y): int(num) for y, line in enumerate(input.splitlines()) for x, num in enumerate(line)}


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    coords = prepare_coords_dict(input)
    return sum(num + 1 for (x, y), num in coords.items() if all_adjacent_cords_are_lower(x, y, num, coords))


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    coords = prepare_coords_dict(input)
    low_points = [((x, y), num) for (x, y), num in coords.items() if all_adjacent_cords_are_lower(x, y, num, coords)]
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
    return basins[-1] * basins[-2] * basins[-3]
