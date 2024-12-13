""" 
Advent of Code 2024
Day 13: Claw Contraption
"""

import time
import numpy as np

t0 = time.time()

# Open file and read content
f = open("input.txt", "r")
lines = f.readlines()
f.close()

machine_list = []
machine = []
for line in lines:
    if line.replace("\n", "") != "":  # New machine
        machine.append(line.replace("\n", ""))
    else:
        machine_list.append(machine)
        machine = []
machine_list.append(machine)


# Part 1
# A button: 3 tokens
# B button: 1 token
# No more than 100 times push per button
def cal_button_presses(machine_list):
    total = 0
    for machine in machine_list:
        buttons = []
        for line in machine:
            if line[0] == "B":
                X_cor = int(line.split(": ")[1].split(",")[0][2:])
                Y_cor = int(line.split(": ")[1].split(",")[1][3:])
                buttons.append([X_cor, Y_cor])
            else:
                prize_X = int(line.split(": ")[1].split(",")[0][2:])
                prize_y = int(line.split(": ")[1].split(",")[1][3:])
                prize = np.array([prize_X, prize_y])  # target position
        button_arry = np.array(
            [[buttons[0][0], buttons[1][0]], [buttons[0][1], buttons[1][1]]]
        )

        press_a, press_b = np.linalg.solve(button_arry, prize)
        total += valid_presses(press_a, press_b)
    return total


def valid_presses(press_a, press_b):
    if round(press_a % 1, 2) == 0.99 or round(press_a % 1, 2) == 1.0:
        press_a = round(press_a)
    elif round(press_a % 1, 2) == 0.00:
        press_a = round(press_a)
    else:
        return 0
    if round(press_b % 1, 2) == 0.99 or round(press_b % 1, 2) == 1.0:
        press_b = round(press_b)
    elif round(press_b % 1, 2) == 0.00:
        press_b = round(press_b)
    else:
        return 0

    return press_a * 3 + press_b


total = cal_button_presses(machine_list)
print("The solution for part one is:", total)  # test = 480, input = 34787

# Part 2
# Add 10000000000000 to the X and Y position of every prize


def cal_button_presses2(machine_list):
    total = 0
    for machine in machine_list:
        buttons = []
        for line in machine:
            if line[0] == "B":
                X_cor = int(line.split(": ")[1].split(",")[0][2:])
                Y_cor = int(line.split(": ")[1].split(",")[1][3:])
                buttons.append([X_cor, Y_cor])
            else:
                prize_X = int(line.split(": ")[1].split(",")[0][2:])
                prize_y = int(line.split(": ")[1].split(",")[1][3:])
                prize = np.array(
                    [prize_X + 10000000000000, prize_y + 10000000000000]
                )  # target position
        button_arry = np.array(
            [[buttons[0][0], buttons[1][0]], [buttons[0][1], buttons[1][1]]]
        )

        press_a, press_b = np.linalg.solve(button_arry, prize)
        total += valid_presses(press_a, press_b)
    return total


total = cal_button_presses2(machine_list)
print("The solution for part two is:", total)
10000000000000
t1 = time.time()
print("Time to run this code block is", round(t1 - t0, 4), "seconds")
