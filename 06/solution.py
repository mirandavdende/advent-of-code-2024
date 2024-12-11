""" 
Advent of Code 2024
Day 6: Guard Gallivant
"""

import time

t0 = time.time()

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

content = []
for l in lines:
    content.append(l.replace("\n", ""))

# Part 1
# ^ = guard position and direction
# If # is directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.


def walking(content):
    guard = find_guard(content)
    in_map = True
    while in_map:
        if not eddit_map(guard, content):
            in_map = False
    return content


def find_guard(content):
    row_n = 0
    for row in content:
        column_n = 0
        for column in row:
            if column == "^":
                guard = [row_n, column_n, "^"]
                continue
            if column == ">":
                guard = [row_n, column_n, ">"]
                continue
            if column == "v":
                guard = [row_n, column_n, "v"]
                continue
            if column == "<":
                guard = [row_n, column_n, "<"]
                continue
            column_n += 1
        row_n += 1
    return guard


def move_guard(guard, content):
    if guard[2] == "^":
        guard[0] -= 1
        try:
            if content[guard[0]][guard[1]] == "#":
                # print("hit wall")
                guard[0] += 1
                guard[2] = ">"
        except:
            # print("out of bounds")
            return False
    elif guard[2] == ">":
        guard[1] += 1
        try:
            if content[guard[0]][guard[1]] == "#":
                # print("hit wall")
                guard[1] -= 1
                guard[2] = "v"
        except:
            # print("out of bounds")
            return False
    elif guard[2] == "v":
        guard[0] += 1
        try:
            if content[guard[0]][guard[1]] == "#":
                # print("hit wall")
                guard[0] -= 1
                guard[2] = "<"
        except:
            # print("out of bounds")
            return False
    elif guard[2] == "<":
        guard[1] -= 1
        try:
            if content[guard[0]][guard[1]] == "#":
                # print("hit wall")
                guard[1] += 1
                guard[2] = "^"
        except:
            # print("out of bounds")
            return False
    return guard


def eddit_map(guard, content):
    content[guard[0]] = (
        content[guard[0]][: guard[1]] + "X" + content[guard[0]][guard[1] + 1 :]
    )
    new_guard = move_guard(guard, content)
    if new_guard:
        content[new_guard[0]] = (
            content[new_guard[0]][: new_guard[1]]
            + new_guard[2]
            + content[new_guard[0]][new_guard[1] + 1 :]
        )
    else:
        return False
    return content


total = 0
for line in walking(content):
    for char in line:
        if char == "X":
            total += 1


print("The solution for part one is:", total)  # test = 41, input = 5208

# Part 2

total = 0
print("The solution for part two is:", total)


t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
