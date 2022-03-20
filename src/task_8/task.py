# **************************************** PART ONE ****************************************
def first_subtask(input: str) -> int:
    count = 0
    for line in input.splitlines():
        _, output = line.split("|")
        digits = output.split()
        count += sum(len(digit) in {2, 3, 4, 7} for digit in digits)
    return count


# **************************************** PART TWO ****************************************
def contains_all_chars(digit: list[str], second_digit: list[str]) -> bool:
    return all(char in digit for char in second_digit)


def second_subtask(input: str) -> int:
    result = 0
    for line in input.splitlines():
        input_digits, output_digits = line.split("|")
        input_digits = sorted([sorted(digit) for digit in input_digits.split()], key=len)
        output_digits = ["".join(sorted(digit)) for digit in output_digits.split()]
        num_to_digit = {}

        for digit in input_digits:
            match len(digit):
                case 2:
                    num_to_digit[1] = digit
                case 3:
                    num_to_digit[7] = digit
                case 4:
                    num_to_digit[4] = digit
                case 5:
                    if contains_all_chars(digit, num_to_digit[1]):
                        num_to_digit[3] = digit
                    elif sum(char in digit for char in num_to_digit[4]) == 3:
                        num_to_digit[5] = digit
                    else:
                        num_to_digit[2] = digit
                case 6:
                    if not contains_all_chars(digit, num_to_digit[1]):
                        num_to_digit[6] = digit
                    elif contains_all_chars(digit, num_to_digit[4]):
                        num_to_digit[9] = digit
                    else:
                        num_to_digit[0] = digit
                case 7:
                    num_to_digit[8] = digit

        digit_to_num = {"".join(v): k for k, v in num_to_digit.items()}
        result += sum(10 ** (3 - i) * digit_to_num[output_digits[i]] for i in range(4))
    return result
