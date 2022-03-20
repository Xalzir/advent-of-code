from collections import Counter


def get_points_cords_per_line(input) -> tuple[int, int, int, int]:
    for line in input.splitlines():
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        yield int(x1), int(y1), int(x2), int(y2)


def count_result(scores_per_cords: Counter[tuple[int, int]]) -> int:
    counter = 0
    for _, count in scores_per_cords.most_common():
        if count > 1:
            counter += 1
        else:
            break
    return counter


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    point_counter = Counter()
    for (x1, y1, x2, y2) in get_points_cords_per_line(input):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point_counter[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point_counter[x, y1] += 1
    return count_result(point_counter)


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    point_counter = Counter()
    for (x1, y1, x2, y2) in get_points_cords_per_line(input):
        if x1 < x2:
            x_d = 1
        elif x1 > x2:
            x_d = -1
        else:
            x_d = 0
        if y1 < y2:
            y_d = 1
        elif y1 > y2:
            y_d = -1
        else:
            y_d = 0

        x, y = x1, y1
        while (x, y) != (x2 + x_d, y2 + y_d):
            point_counter[(x, y)] += 1
            x, y = x + x_d, y + y_d
    return count_result(point_counter)
