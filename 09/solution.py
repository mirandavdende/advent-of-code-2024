""" 
Advent of Code 2024
Day 9: Disk Fragmenter
"""

import time

t0 = time.time()

# Open file and read content
f = open("test.txt", "r")
lines = f.readlines()
f.close()
disk_map = lines[0].replace("\n", "")

# Part 1
# The digits alternate between indicating the length of a file and the length of free space
files = []


def append_file(line, file_n):
    file = []
    for i in range(int(line)):
        file.append(file_n)
    files.append(file)


def append_free_space(line):
    free_space = []
    for i in range(int(line)):
        free_space.append(".")
    files.append(free_space)


def rearange_files(files):
    print(files)
    input_n = 0
    for file in files:

        if "." in file:
            count = len(file)
            print(count)
            for n in range(count):
                for f in files[::-1]:
                    if "." not in f:
                        print(len(f), n)
                        if len(f) > n:
                            files[input_n][n] = f[n]
                        else:

                            continue
                        print(files[input_n], f)
                    # my_list[i] = "orange"
        input_n += 1


file_n = 0
for l in range(len(disk_map)):
    if l % 2 == 0:
        # print("length of file", file_n, "is", disk_map[l])
        append_file(disk_map[l], file_n)
        file_n += 1
    else:
        # print("length of free space", disk_map[l])
        append_free_space(disk_map[l])

rearange_files(files)

total = 0
print("The solution for part one is:", total)

# Part 2

total = 0
print("The solution for part two is:", total)  # test = 1928

t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
