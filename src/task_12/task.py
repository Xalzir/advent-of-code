from collections import defaultdict


def prepare_edges_with_neighbours(input: str) -> defaultdict[str, set[str]]:
    edges = defaultdict(set)
    for src, dest in [line.split("-") for line in input.splitlines()]:
        edges[src].add(dest)
        edges[dest].add(src)
    return edges


# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    edges = prepare_edges_with_neighbours(input)
    paths = set()
    unfinished_paths = [("start",)]

    while unfinished_paths:
        path = unfinished_paths.pop()

        if path[-1] == "end":
            paths.add(path)
            continue

        for neighbour in edges[path[-1]]:
            if neighbour.isupper() or neighbour not in path:
                unfinished_paths.append((*path, neighbour))

    return len(paths)


# **************************************** PART TWO ****************************************
def is_lowercase_double_visited(path: list[str]) -> bool:
    return any(path.count(edge) > 1 for edge in path if edge.islower())


def second_subtask(input: str) -> int:
    edges = prepare_edges_with_neighbours(input)
    paths = set()
    unfinished_paths = [("start",)]

    while unfinished_paths:
        path = unfinished_paths.pop()

        if path[-1] == "end":
            paths.add(path)
            continue

        for neighbour in edges[path[-1]]:
            if (
                neighbour.isupper() or neighbour not in path or not is_lowercase_double_visited(path)
            ) and neighbour != "start":
                unfinished_paths.append((*path, neighbour))

    return len(paths)
