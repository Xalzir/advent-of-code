from typing import Iterator


def adjacent_cords(x: int, y: int) -> Iterator[tuple[int, int]]:
    return ((x + x_diff, y + y_diff) for x_diff in (-1, 0, 1) for y_diff in (-1, 0, 1) if x_diff != 0 or y_diff != 0)


def prepare_coords_from_input(input: str) -> dict[tuple[int, int], int]:
    return {(x, y): int(num) for y, line in enumerate(input.splitlines()) for x, num in enumerate(line)}


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    flashes = 0
    coords = prepare_coords_from_input(input)
    for _ in range(100):
        flash_coords = []
        for k in coords:
            coords[k] += 1
            if coords[k] > 9:
                flash_coords.append(k)

        while flash_coords:
            pt = flash_coords.pop()
            if coords[pt] == 0:
                continue
            coords[pt] = 0
            flashes += 1
            for adjanced in adjacent_cords(*pt):
                if adjanced in coords and coords[adjanced] != 0:
                    coords[adjanced] += 1
                    if coords[adjanced] > 9:
                        flash_coords.append(adjanced)
    return flashes


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    coords = prepare_coords_from_input(input)
    iteration = 0
    while True:
        iteration += 1
        flash_coords = []
        for k in coords:
            coords[k] += 1
            if coords[k] > 9:
                flash_coords.append(k)

        while flash_coords:
            pt = flash_coords.pop()
            if coords[pt] == 0:
                continue
            coords[pt] = 0
            for adjanced in adjacent_cords(*pt):
                if adjanced in coords and coords[adjanced] != 0:
                    coords[adjanced] += 1
                    if coords[adjanced] > 9:
                        flash_coords.append(adjanced)

        if all(value == 0 for value in coords.values()):
            break

    return iteration
