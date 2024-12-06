""" 
Advent of Code 2024
Day 4: Ceres Search
"""

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

content = []
for l in lines:
    content.append(l.replace("\n", ""))

# Part 1
# Lookling for the word XMAS
# horizontal
# horizontal, backwards
# vertical
# vertical, backwards
# diagonal, left to right
# diagonal, left to right, backwards
# diagonal, right to left
# diagonal, right to left, backwards


def check_word(input, word):
    count = 0
    for i in input:
        start = 0
        while True:
            start = i.find(word, start)
            if start == -1:
                break
            # print("found", word, "at", i)
            count += 1
            start += len(word)  # Move past the current found word
    return count


def reversed_list(input):
    reversed_list = []
    for s in input:
        # print(s[::-1])
        reversed_list.append(s[::-1])
    return reversed_list


def make_vertical(input):
    vertical = []
    for i in range(len(input[0])):  # Length of the strings (number of columns)
        # Join the i-th character of each string to form a new string
        new_string = "".join(row[i] for row in input)
        # Append the new string to the vertical list
        vertical.append(new_string)
    return vertical


def make_diagonal(input):
    diagonals = []
    for i in range(len(input[0])):
        diagonal = ""
        for j in range(len(input) - i):
            diagonal += input[j][j + i]
        diagonals.append(diagonal)
    count = 0
    for i in range(len(input[0])):
        diagonal = ""
        for j in range(-i - 1, len(input) - i, 1):
            if j > 0:
                diagonal += input[j + count][j - 1]
        count += 1
        diagonals.append(diagonal)
    return diagonals


def make_diagonal2(input):
    diagonals = []
    for i in range(len(input[0])):
        count = 0
        diagonal = ""
        for j in range(len(input) - i, 0, -1):
            diagonal += input[count][j - 1]
            # print(input[count], count, j - 1, input[count][j - 1])
            count += 1
        diagonals.append(diagonal)
    for i in range(len(input[0])):
        count = 1
        diagonal = ""
        for j in range(len(input) - 1, 0, -1):
            if j > i:
                diagonal += input[count + i][j]
                count += 1
        diagonals.append(diagonal)
    return diagonals


def permutations_check(input, word):
    count = 0
    count += check_word(input, word)
    # print("After horizontal", count)  # 3
    count += check_word(reversed_list(input), word)
    # print("After horizontal, backwards", count)  # 2, total = 5

    count += check_word(make_vertical(input), word)
    # print("After vertical", count)  # 1, total = 6
    count += check_word(reversed_list(make_vertical(input)), word)
    # print("After vertical, backwards", count)  # 2, total = 8

    count += check_word(make_diagonal(input), word)
    # print("After diagonal, left to right", count)  # 1
    count += check_word(reversed_list(make_diagonal(input)), word)
    # print("After diagonal, left to right, backwards", count)  # 4

    count += check_word(make_diagonal2(input), word)
    # print("After diagonal, right to left", count)  # 1
    count += check_word(reversed_list(make_diagonal2(input)), word)
    # print("After diagonal, right to left, backwards", count)  # 4

    return count


total = permutations_check(content, "XMAS")
print("The solution for part one is:", total)  # test = 18, input = 2633

# Part 2
# MAS has to be written in a X, forward or backward

total = 0
print("The solution for part two is:", total)  # test = 9
