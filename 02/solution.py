""" 
Advent of Code 2024
Day 2: Red-Nosed Reports
"""

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

content = []
for l in lines:
    content.append(l.replace("\n", ""))

clean_content = []

for l in content:
    line = []
    for n in l.split():
        line.append(int(n))
    clean_content.append(line)

# Part 1
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def valid_report(report):
    safe = True
    last = report[0]
    last_diff = 0
    for current in report[1:]:
        diff = int(current) - last
        if int(current) - last > 3 or int(current) - last < -3:
            safe = False
            break
        elif int(current) - last == 0:
            safe = False
            break
        elif (diff < 0 and last_diff > 0) or (diff > 0 and last_diff < 0):
            safe = False
            break
        last = int(current)
        last_diff = diff
    return safe


total = 0
for l in clean_content:
    if valid_report(l):
        total += int(valid_report(l))
print("The solution for part one is:", total)

# Part 2
# which reports are safe when removing one level?


def generate_permutations(report):
    new_reports = []
    for i in range(len(report)):
        new = report.copy()
        new.pop(i)
        new_reports.append(new)
    return new_reports


total = 0
for l in clean_content:
    if valid_report(l):
        total += int(valid_report(l))
    else:
        for r in generate_permutations(l):
            if valid_report(r):
                total += int(valid_report(r))
                break


print("The solution for part two is:", total)
