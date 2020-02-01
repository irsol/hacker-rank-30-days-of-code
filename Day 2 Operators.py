#!/bin/python3

import math
import os
import random
import re
import sys

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal 
# price being added as tip), and tax percent (the percentage of the meal price being added as tax)
# for a meal, find and print the meal's total cost.

# Output Format
#
# Print the total meal cost, where totalCost is the rounded integer result of the entire bill (totalCost with added
# tax and tip).

# Sample Input
"""
12.00
20
8
"""

# Sample Output
"""
15
"""

# Explanation

# Given:
# mealCost = 12, tipPercent = 20, taxPercent = 20

# Calculations:
"""
tip = 12*20/100 = 2.4
tax = 12*8/100 = 0.96

totalCost = mealCost + tip + tax = 12 + 2.4 + 0.96 = 15.36
round(totalCost) = 15
We round totalCost to the nearest dollar (integer) and then print our result, 15.
"""


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
