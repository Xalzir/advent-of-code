def get_input(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data
