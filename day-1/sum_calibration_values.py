import sys


def read_and_sum_input_values(filepath):
    """
    returns the sum of all decoded lines in input text
    """

    sum = 0
    with open(filepath, "r") as file:
        for line in file:
            print("input_line=", line)
            sum += decode_calibration_value(line)

    return sum


def decode_calibration_value(line):
    """
    decodes two-digit value from a line of text by combining
    the first and last digits found
    "1fde3fd" -> "13"
    """

    digits = "0123456789"

    calibration_value = ""

    # first digit:
    for char in line:
        if char in digits:
            calibration_value += char
            break

    # second digit:
    for char in line[::-1]:
        if char in digits:
            calibration_value += char
            break

    return int(calibration_value)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("file path needed: python sum_valibration_values.py <file_path>")
    else:
        filepath = sys.argv[1]
        sum = read_and_sum_input_values(filepath)
        print("Sum:", sum)
