""" 
Advent of Code 2024
Day 8:
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

total = 0
print("The solution for part two is:", total)

# Part 2

total = 0
print("The solution for part two is:", total)

t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")