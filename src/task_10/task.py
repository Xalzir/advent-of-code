from statistics import median

SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORES_SECOND = {"(": 1, "[": 2, "{": 3, "<": 4}
OPENINGS = ["{", "(", "[", "<"]
CLOSINGS = {"}": "{", ")": "(", "]": "[", ">": "<"}

# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    result = 0
    for line in input.splitlines():
        unclosed = []
        for char in line:
            if char in OPENINGS:
                unclosed.append(char)
            else:
                if CLOSINGS[char] == unclosed[-1]:
                    unclosed.pop()
                else:
                    result += SCORES[char]
                    break

    return result


# **************************************** PART TWO ****************************************
def second_subtask(input: str) -> int:
    results = []
    for line in input.splitlines():
        unclosed = []
        for char in line:
            if char in OPENINGS:
                unclosed.append(char)
            else:
                if CLOSINGS[char] == unclosed[-1]:
                    unclosed.pop()
                else:
                    break
        else:
            score = 0
            for char in reversed(unclosed):
                score *= 5
                score += SCORES_SECOND[char]
            results.append(score)

    return median(results)
