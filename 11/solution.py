""" 
Advent of Code 2024
Day 11: Plutonian Pebbles
"""

import time

t0 = time.time()

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

content = []
for l in lines:
    for n in l.split():
        content.append(int(n))


# Part 1
# Engraved with number 0: replaced by number 1
# Engraved with number that has an even number of digits: replaced by two numbers split in the middle (no leading 0)
# If none of the other rules apply: replaced by a new stone, number multiplied by 2024
def rule1(stone):
    stone = 1
    return stone


def rule2(stone):
    # Find the middle index
    str_num = str(stone)
    mid = len(str_num) // 2

    # Split the stone at the middle
    first_stone = str_num[:mid]
    second_stone = str_num[mid:]

    return int(first_stone), int(second_stone)


def rule3(stone):
    stone = stone * 2024
    return stone


def blinking(content, blink_n):
    for n in range(blink_n):
        t01 = time.time()
        old_content = content
        content = []
        for stone in old_content:
            str_num = str(abs(stone))
            equal = len(str_num) % 2
            if stone == 0:
                content.append(rule1(stone))
            elif equal == 0:
                new_stone = rule2(stone)
                content.append(new_stone[0])
                content.append(new_stone[1])
            else:
                content.append(rule3(stone))
        t1 = time.time()
        print(
            "N blink",
            n,
            "during",
            round(t1 - t01, 3),
            "seconds and the total time is",
            round(t1 - t0, 3) / 60,
            "minutes",
        )
    return content


blink_n = 25
new_stones = blinking(content, blink_n)
total = len(new_stones)

print("The solution for part one is:", total)  # test = 55312, input = 229043

# Part 2
blink_n = 75
new_stones = blinking(content, blink_n)
total = len(new_stones)
print("The solution for part two is:", total)

t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
