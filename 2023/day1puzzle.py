import re

number_map = {
    # "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def puzzle1(word_list):
    endValue = 0
    for line in word_list:
        line_value = ""
        digit_list = []
        for char in line:
            if char.isdigit() == True:
                digit_list += char
        line_value = "".join([digit_list[0], digit_list[-1]])
        endValue += int(line_value)
    print(f"Puzzle1 Value: {endValue}")


def puzzle2(word_list):
    endValue = 0
    for line in word_list:
        line_value = ""
        digit_list = []
        line = append_numbers(line)
        for char in line:
            if char.isdigit() == True:
                digit_list += char
        line_value = "".join([digit_list[0], digit_list[-1]])
        endValue += int(line_value)
    print(f"Puzzle2 Value: {endValue}")


# Function to append numbers to the left of the match for cases like "eightree"
def append_numbers(s):
    matches = []
    # Find all matches of each word in the string
    for word, number in number_map.items():
        matches.extend((m.start(), number) for m in re.finditer(word, s))

    # Sort matches in reverse order by their start position
    matches.sort(key=lambda x: x[0], reverse=True)

    # Append the numbers in reverse order to avoid changing the positions of later matches
    for position, number in matches:
        s = s[:position] + number + s[position:]

    return s


if __name__ == "__main__":
    with open("day1input.txt") as f:
        word_list = f.readlines()
        puzzle1(word_list)
        puzzle2(word_list)
