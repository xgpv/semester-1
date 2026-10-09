# Worksheet 1.2: Task 2 Solution

import sys

from util import read_numbers

try:
    numbers = read_numbers()
except ValueError:
    sys.exit('Error: no numbers provided')
numbers = sorted(numbers)
median = len(numbers) // 2
if median == float
print(numbers[median])

print(f'Minimum = {min(numbers)} \nMaximum = {max(numbers)} \nMean = {sum(numbers)/len(numbers)} ')