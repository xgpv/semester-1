# Worksheet 1.2: Task 2 Solution

import sys

from util import read_numbers

try:
    numbers = read_numbers()
except ValueError:
    sys.exit('Error: no numbers provided')

numbers = sorted(numbers)

#Calculating Median
median = len(numbers) // 2
if (len(numbers)) % 2 == 0:
    medianminus = median - 1
    median = (numbers[median] + numbers[medianminus]) / 2


print(f'Minimum = {min(numbers)} \nMaximum = {max(numbers)} \nMean = {sum(numbers)/len(numbers)} \nMedian = {median}')