""" 
Advent of Code 2024
Day 7: Bridge Repair
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
import operator
from itertools import product


def calculate_mixed(sum, number_list, operators):
    # Create all combinations of operators for n-1 operators (where n is the length of numbers)
    operator_combinations = product(operators, repeat=len(number_list) - 1)

    results = []
    for op_comb in operator_combinations:
        # Create the expression based on the numbers and current operator combination
        expression = str(number_list[0])
        for i in range(1, len(number_list)):
            expression += f" {op_comb[i-1]} {number_list[i]}"

        # Evaluate the expression
        tokens = expression.split()

        # Initialize the result with the first number
        result = int(tokens[0])

        # Iterate through the remaining tokens, which are pairs of operator and number
        for i in range(1, len(tokens), 2):
            operator = tokens[i]
            number = int(tokens[i + 1])

            # Perform the operation from left to right
            if operator == "+":
                result += number
            elif operator == "||":
                result = str(result) + str(number)
                result = int(result)
            elif operator == "*":
                result *= number
        results.append(result)
    return results


total = 0
for line in content:
    sum = int(line.split(":")[0])
    numbers = line.split(":")[1]
    number_list = []
    for number in numbers.split(" "):
        try:
            if number != "":
                number_list.append(int(number))
        except:
            pass
    # print("Numbers in this line:", len(number_list), "for numbers", number_list, "with a sum of", sum)
    operators = ["+", "*"]
    results = calculate_mixed(sum, number_list, operators)
    # print("Results:", results)
    for result in results:
        if result == sum:
            total += sum
            # print("number added", result)
            break


print("The solution for part two is:", total)  # test = 3749, input = 303766880536

# Part 2
total = 0
for line in content:
    sum = int(line.split(":")[0])
    numbers = line.split(":")[1]
    number_list = []
    for number in numbers.split(" "):
        try:
            if number != "":
                number_list.append(int(number))
        except:
            pass
    # print("Numbers in this line:", len(number_list), "for numbers", number_list, "with a sum of", sum)
    operators = ["+", "*", "||"]
    results = calculate_mixed(sum, number_list, operators)
    # print("Results:", results)
    for result in results:
        if result == sum:
            total += sum
            # print("number added", result)
            break

print("The solution for part two is:", total)  # test = 11387, input = 337041851384440

t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
