def get_input() -> list[str]:
    with open("input.txt") as data:
        return data.read().splitlines()


input = get_input()

# **************************************** PART ONE ****************************************
count = 0
for line in input:
    _, output = line.split(" | ")
    digits = output.split()
    count += sum(len(digit) in {2, 3, 4, 7} for digit in digits)

print(f"result for first subtask: {count}")

# **************************************** PART TWO ****************************************
