""" 
Advent of Code 2024
Day 5: Print Queue
"""

import time

t0 = time.time()

# Open file and read content
f = open("test.txt", "r")
lines = f.readlines()
f.close()

ordering = []
pages_lists = []
for l in lines:
    l = l.replace("\n", "")
    if "|" in l:
        update = []
        for page in l.split("|"):
            update.append(int(page))
        ordering.append(update)
    elif "," in l:
        update = []
        for page in l.split(","):
            update.append(int(page))
        pages_lists.append(update)

# Part 1
# First section = page ordering rules
# X|Y --> if both number X and number Y are in an update, page number X must be printed at some point before page number Y
# Second section = pages to produce in each update (one per line)
# Sum of the middle page number of each correctly-ordered update

total = 0


def correctly_ordered(ordering, pages):
    pairs_to_check = []
    for page in pages:
        # Check if page is in the ordering list
        for pair in ordering:
            if page in pair:
                # print("Page", page, "is in ordering list", pair)
                # Check if both pages are in the ordering list
                if pair[0] in pages and pair[1] in pages:
                    if pair not in pairs_to_check:
                        # print("Both pages are in the ordering list of pair", pair)
                        pairs_to_check.append(pair)
    # Check if page is before other page
    for pair in pairs_to_check:
        if pages.index(pair[0]) > pages.index(pair[1]):
            return False
    return True


def get_middle_page(pages):
    return pages[len(pages) // 2]


good_updates = []
for pages in pages_lists:
    if correctly_ordered(ordering, pages):
        good_updates.append(pages)

for update in good_updates:
    total += get_middle_page(update)

print("The solution for part one is:", total)  # test = 143, input = 5639

# Part 2
total = 0


def order_pages(ordering, pages):
    pairs_to_check = []
    for page in pages:
        for pair in ordering:
            if page in pair:
                # print("Page", page, "is in ordering list", pair)
                if pair[0] in pages and pair[1] in pages:
                    if pair not in pairs_to_check:
                        pairs_to_check.append(pair)
    # reorder pages
    for pair in pairs_to_check:
        if pages.index(pair[0]) > pages.index(pair[1]):
            print(pages)
            print(pair, pages.index(pair[0]), pages.index(pair[1]))


bad_updates = []
for pages in pages_lists:
    order_pages(ordering, pages)

print("The solution for part two is:", total)  # test = 123

t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
