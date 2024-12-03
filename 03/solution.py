""" 
Advent of Code 2024
Day 3: Mull It Over
"""

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()
text = str(lines)

# Part 1
import re


# Loop to find all occurrences of a word
def find_mul(text, word):
    start = 0
    positions = []
    word = word
    while True:
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += len(word)  # Move past the current found word
    return positions


# Find all mul() and make a list
def end_mul(positions):
    possible_muls = []
    char_to_find = ")"
    for position in positions:
        end_position = text.find(char_to_find, position)
        mul = text[position : end_position + 1]  # Slice from start to end_position
        possible_muls.append(text[position : end_position + 1])
    return possible_muls


# Test if the mul is good of bad
def test_string(item):
    # Define the regex pattern
    pattern = r"^mul\((-?\d+),(-?\d+)\)$"
    # Use re.match to check if the pattern matches the whole string
    if re.match(pattern, item):
        return True
    else:
        return False


# Extract the numbers from the string
def get_numbers(item):
    numbers = []
    for i in re.split(r"[(,)]", item):
        try:
            numbers.append(int(i))
        except:
            pass
    return numbers


positions = find_mul(text, "mul(")
possible_muls = end_mul(positions)
total = 0
for item in possible_muls:
    if test_string(item):
        total += get_numbers(item)[0] * get_numbers(item)[1]

print("The solution for part one is:", total)


# Part 2
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
def test_do_dont_mul(dos, donts, muls):
    valid_muls = []
    i_do = 0
    i_dont = 0
    for i in range(len(muls)):
        while muls[i] > dos[i_do + 1]:
            i_do += 1
            # print("dos increased to", dos[i_do], "because of", muls[i])
            while dos[i_do] > donts[i_dont]:
                i_dont += 1
                # print("donts increased to", donts[i_dont], "because of", muls[i])
        if muls[i] > dos[i_do] and muls[i] < donts[i_dont]:
            valid_muls.append(muls[i])
            # print(muls[i], "between", dos[i_do], "and", donts[i_dont])
        else:
            False
    return valid_muls


positions_do = find_mul(text, "do()")
positions_do.insert(0, 0)
positions_do.append(len(text))
positions_dont = find_mul(text, "don't()")
positions_dont.append(len(text))

positions2 = test_do_dont_mul(positions_do, positions_dont, positions)

possible_muls = end_mul(positions2)
total = 0
for item in possible_muls:
    if test_string(item):
        total += get_numbers(item)[0] * get_numbers(item)[1]

print("The solution for part two is:", total)
# 6920860 to low
# 53783319 --> good
# 156616081 to high
