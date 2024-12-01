""" 
Advent of Code 2024
Day 1: Historian Hysteria
"""

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

# Part 1
# Make two lists
l1 = []
l2 = []
for l in lines:
    l1.append(int(l.split()[0]))
    l2.append(int(l.split()[1]))

# Sort the lists
l1.sort()
l2.sort()

# Caluculate the diffferences
differences = []
for a, b in zip(l1, l2):
    differences.append(abs(a - b))

# Sum the differences
total = sum(differences)
print("The solution for part one is:", total)

# Part 2
# Count the similar numbers
sim = []
for n in l1:
    count = l2.count(n)
    sim.append(n * count)

total = sum(sim)
print("The solution for part two is:", total)
